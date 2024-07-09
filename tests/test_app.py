import pytest
from app import app
from lib.models.user import User
from lib.models.property import Property
from lib.repositories.property_repository import PropertyRepository

# Sample property data as instances of Property model
property_data = [
    Property(1, "Studio in London", "Great studio to rent in the heart of London", 60.0, '2024-07-01', '2024-12-31', 1),
    Property(2, "Spacious Apartment", "Lovely spacious apartment with great views", 80.0, '2024-08-01', '2024-11-30', 2),
    Property(3, "Modern Flat", "Newly renovated modern flat in city center", 100.0, '2024-09-01', '2024-10-31', 3),
    Property(4, "Cozy Cottage", "A cozy cottage in the countryside", 40.0, '2024-07-15', '2024-12-15', 4),
    Property(5, "Beach House", "Beautiful beach house with ocean views", 120.0, '2024-07-01', '2024-08-31', 5),
]

# Sample user data as instances of User model
user_data = [
    User(1, "martha.hudson@example.com", "Martha Hudson", "IamSHerl0ck3d"),
    User(2, "homer.simpson@example.com", "Homer Simpson", "d0h12345"),
    User(3, "sirius.black@example.com", "Sirius Black", "padf00t123"),
    User(4, "bruce.wayne@example.com", "Bruce Wayne", "batc4ve123"),
    User(5, "bilbo.baggins@example.com", "Bilbo Baggins", "ringbearer123"),
]

@pytest.fixture
def property_repository():
    """
    Fixture that provides a mock of PropertyRepository.
    """
    class MockPropertyRepository(PropertyRepository):
        def __init__(self):
            self.properties = property_data
        
        def all(self):
            return self.properties
        
        def find_by_id(self, id):
            for property in self.properties:
                if property.id == id:
                    return property
            return None
    
    return MockPropertyRepository()

@pytest.fixture
def user_repository():
    """
    Fixture that provides a mock of UserRepository.
    """
    class MockUserRepository:
        def __init__(self):
            self.users = user_data
        
        def all(self):
            return self.users
        
        def find_by_id(self, id):
            for user in self.users:
                if user.id == id:
                    return user
            return None
    
    return MockUserRepository()

def test_get_all_properties(property_repository):
    """
    Test case for retrieving all properties using the property repository fixture.
    """
    properties = property_repository.all()
    assert len(properties) == len(property_data)
    for property in property_data:
        assert property in properties

def test_property_detail_route(property_repository):
    """
    Test case for retrieving a specific property by ID using the property repository fixture.
    """
    property = property_repository.find_by_id(1)
    assert property is not None
    assert property.id == 1
    assert property.name == "Studio in London"
    assert property.description == "Great studio to rent in the heart of London"
    assert property.owner_id == 1

    property = property_repository.find_by_id(999)
    assert property is None
