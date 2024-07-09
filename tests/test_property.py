from lib.models.property import *
from datetime import datetime
def test_property_init():
    property = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)

    assert property.id == 1
    assert property.name == '123 Main Street'
    assert property.price == 45
    assert property.description == 'This is a house'
    assert property.available_from == datetime(2024, 1, 1)
    assert property.available_to == datetime(2024, 1, 31)
    assert property.owner_id == 1

def test_property_str_repr():
    property = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    assert str(property) == 'Property(1, 123 Main Street,  This is a house, 45, 2024-01-01 00:00:00, 2024-01-31 00:00:00, 1)'

def test_eq():
    property = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    assert property == Property(1, '123 Main Street', 'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)

def test_is_valid():
    property = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    property2 = Property(1, '',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    property3 = Property(1, '123 Main Street',  None, 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    property4 = Property(1, '123 Main Street',  'This is a house', None, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    property5 = Property(1, '123 Main Street',  'This is a house', 45, None, datetime(2024, 1, 31), 1)
    property6 = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), None, 1)
    assert property.is_valid() == True
    assert property2.is_valid() == False
    assert property3.is_valid() == False
    assert property4.is_valid() == False
    assert property5.is_valid() == False
    assert property6.is_valid() == False

def test_generate_errors():
    property = Property(1, '',  '', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    assert property.generate_errors() == "You must enter a name, You must enter a description"
    property2 = Property(1, '123 Main Street',  'This is a house', 0, None, datetime(2024, 1, 31), 1)
    assert property2.generate_errors() == "You must enter a price, You must enter a valid date"


