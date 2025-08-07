import pytest
from src import Inventory

def test_add_stock():
    inv = Inventory()
    inv.add_stock("apple",50)
    assert inv.stock["apple"] == 50
    inv.add_stock("apple",20)
    assert inv.stock["apple"] == 70
    
def test_remove_stock():
    inv = Inventory()
    inv.add_stock("apple",70)
    inv.remove_stock("apple",10)
    assert inv.stock["apple"] == 60
    
    with pytest.raises(ValueError):
        inv.remove_stock("apple",100)

def test_check_availability():
    inv = Inventory()
    inv.add_stock("apple",120)
    assert inv.check_availability("apple",30) is True
    
def test_full():
    inv = Inventory()
    inv.add_stock("apple",50)
    assert inv.stock["apple"] == 50
    inv.remove_stock("apple",10)
    assert inv.stock["apple"] == 40
    assert inv.check_availability("apple",30) is True
    assert inv.check_availability("apple",50) is False
   