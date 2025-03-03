import pytest
from products import Product

def test_creating_prod():
    """
    Test that creates a normal product works.
    """
    prod =  Product("Max34r", price=1450, quantity=100)
    assert isinstance(prod, Product)

def test_creating_prod_invalid_details():
    """
    Test that creating a product with empty name.Raises exception
    """
    with pytest.raises(ValueError, match="Enter valid input: name must be non-empty,"
                                         " price > 0, and quantity >= 0"):
        Product("", price=1450, quantity=100)


def test_prod_becomes_negative():
    """
    Test that creating a product with negative quantity.Raises exception
    """
    with pytest.raises(ValueError, match="Enter valid input: name must be non-empty,"
                                         " price > 0, and quantity >= 0"):
        Product("", price=1450, quantity=100)


def test_modifies_quantity():
    """
    Test that product purchase modifies the quantity and returns the right output.
    """
    prod = Product("MacBook Air M2", price=10, quantity=100)
    current_quantity = prod.quantity
    prod_num_buy = 4
    prod.buy(prod_num_buy)
    updated_quantity = prod.quantity
    assert updated_quantity == current_quantity - prod_num_buy


def test_check_quantity_inactive():
    """
    Test that when a product reaches 0 quantity, it becomes inactive
    """
    prod = Product("MacBook Air M2", price=10, quantity=100)
    prod_num_buy = 100
    prod.buy(prod_num_buy)
    assert prod.is_active() == False


def test_buy_too_much():
    """
    Test that buying a larger quantity than exists invokes exception.
    """
    with pytest.raises(ValueError, match="Error while making order!"
                                         " Quantity larger than what exists"):
        prod = Product("MacBook Air M2", price=10, quantity=10)
        prod_num_buy = 11
        prod.buy(prod_num_buy)
