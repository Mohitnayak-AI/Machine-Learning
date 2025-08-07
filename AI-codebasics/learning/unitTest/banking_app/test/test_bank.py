import pytest
from src.bank import BankAccount

def test_create_account():
    account = BankAccount("Mohit", 100)
    
    assert account.owner == "Mohit"
    assert account.balance == 100
     
def test_deposit():
    account = BankAccount("Raj")
    account.deposit(50)
    account.deposit(40)
    
    assert account.balance == 90
    
    # test the -ve deposit
    with pytest.raises(ValueError):
        account.deposit(-10)
        
def test_withdraw():
    account = BankAccount("Tanu",50)
    account.withdraw(10)
    account.withdraw(10)
    
    assert account.balance == 30
    
    # test for insufficent balance
    with pytest.raises(ValueError):
        account.withdraw(1000)
        
@pytest.mark.skip(reason="xyz reason") # skip the test
def test_balance():
    account = BankAccount("Pallavi",120)
    assert account.get_balance() == 120