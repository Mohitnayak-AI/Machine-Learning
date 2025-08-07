import mysql.connector
from contextlib import contextmanager
from log_setup import setup_log

logger = setup_log('db_helper_log')

@contextmanager
def get_bd_cursor(commit=False):
    connction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Mahakal2090#",
        database = "expense_manager"
    )
    
    cursor = connction.cursor(dictionary=True)
    yield cursor
    if commit:
        connction.commit()
    cursor.close()
    connction.close()
    
def fatch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_bd_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses
    
def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_bd_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",(expense_date,))

def insert_expenses(expense_date,amount,category,notes):
    logger.info(f"insert_expenses called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_bd_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",(expense_date,amount,category,notes))

def fatch_expense_summary(start,end):
    logger.info(f"fatch_expense_summary called start with: {start} and end with {end}")
    with get_bd_cursor() as cursor:
        cursor.execute(
            """SELECT category,sum(amount) as total FROM expense_manager.expenses 
            where expense_date 
            between %s and  %s
            group by category
            order by sum(amount) desc""",
            (start,end)
        )
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    expenses = fatch_expenses_for_date("2024-08-06")
    print(expenses)
    # insert_expenses("2024-08-26",500,"Food","pasta")
    # # delete_expenses_for_date("2024-08-25")
    # summary = fatch_expense_summary("2024-08-01","2024-08-05")
    # for s in summary:
    #     print(s)