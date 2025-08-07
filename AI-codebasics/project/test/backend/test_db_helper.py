from backend import bd_helper

def test_fatch_expenses_for_date():
    expenses = bd_helper.fatch_expenses_for_date("2024-08-15")
    
    assert len(expenses) == 1
    assert expenses[0]["amount"] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]["notes"] == "Bought potatoes"
    
def test_fatch_expenses_for_date_invalid():
    expenses = bd_helper.fatch_expenses_for_date("9999-08-15")
    
    assert len(expenses) == 0
    
def test_fatch_summary_invalid():
    summary = bd_helper.fatch_expense_summary("2099-01-20","2099-02-03")
    assert len(summary) == 0