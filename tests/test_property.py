from lib.models.property import *

def test_property_init():
    property = Property(1, '123 Main Street', 45, 'This is a house', 1)
    assert property.id == 1
    assert property.address == '123 Main Street'
    assert property.price == 45
    assert property.description == 'This is a house'
    assert property.user_id == 1

def test_property_str_repr():
    property = Property(1, '123 Main Street', 45, 'This is a house', 1)
    assert str(property) == 'Property(1, 123 Main Street, 45, This is a house, 1)'

def test_eq():
    property = Property(1, '123 Main Street', 45, 'This is a house', 1)
    assert property == Property(1, '123 Main Street', 45, 'This is a house', 1)