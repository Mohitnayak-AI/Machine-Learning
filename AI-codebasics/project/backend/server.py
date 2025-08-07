from fastapi import FastAPI,HTTPException
from datetime import date
import bd_helper
from typing import List
from pydantic import BaseModel
from log_setup import setup_log

logger = setup_log('server_log')

app = FastAPI()

class Expenses(BaseModel):
    amount : int
    category : str
    notes : str

class DateRange(BaseModel):
    start_date : date
    end_date : date


@app.get("/expenses/{expense_date}", response_model=List[Expenses])
def get_expenses(expense_date:date):
    logger.info(f"Get expenses is called on {expense_date}")
    expenses = bd_helper.fatch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500,detail="Faild to retrived expense summary")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date:date, expenses:List[Expenses]):
    bd_helper.delete_expenses_for_date(expense_date)
    logger.info(f"we added new data on date {expense_date}")
    for expense in expenses:
        bd_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)
        
    return{"message":"Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range:DateRange):
    data = bd_helper.fatch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail="Faild to retrived expense summary")
    total =sum([row['total'] for row in data])
    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']]={
            "total":row['total'],
            "percentage":percentage
        }
    return breakdown
        