from lib.models.booking import *
from lib.models.property import *
from datetime import datetime 
class BookingRepository:
    
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all_unconfirmed(self):
        rows = self._connection.execute("SELECT * FROM bookings WHERE is_confirmed = false")
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['property_id'], row['user_id'], row['requested_from'], row['requested_to'], row['is_confirmed'], row['total_price'], row['created_at'])
            bookings.append(item)
        return bookings
    
    def create(self, booking):
        if self.is_booking_available(booking):
            self._connection.execute("INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) VALUES (%s, %s, %s, %s, %s, %s)", [booking.property_id, booking.user_id, booking.requested_from, booking.requested_to, booking.total_price, booking.created_at])
            return True
        return False

    def find_by_id(self, id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE id = %s", [id])
        if rows:
            row = rows[0]
            return Booking(row['id'], row['property_id'], row['user_id'], row['requested_from'], row['requested_to'], row['is_confirmed'], row['total_price'], row['created_at'])
        return False
    
    def confirm_booking(self, id):
        self._connection.execute("UPDATE bookings SET is_confirmed = true WHERE id = %s", [id])
    
    def all_confirmed(self):
        rows = self._connection.execute("SELECT * FROM bookings WHERE is_confirmed = true")
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['property_id'], row['user_id'], row['requested_from'], row['requested_to'], row['is_confirmed'], row['total_price'], row['created_at'])
            bookings.append(item)
        return bookings
    
    def all_bookings_of_user(self, user_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE user_id = %s", [user_id])
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['property_id'], row['user_id'], row['requested_from'], row['requested_to'], row['is_confirmed'], row['total_price'], row['created_at'])
            bookings.append(item)
        return bookings
    
    def all_bookings_of_property(self, property_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE property_id = %s", [property_id])
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['property_id'], row['user_id'], row['requested_from'], row['requested_to'], row['is_confirmed'], row['total_price'], row['created_at'])
            bookings.append(item)
        return bookings
    
    def is_booking_available(self, booking):
        # Fetch the property details
        rows = self._connection.execute('SELECT * FROM properties WHERE id = %s', [booking.property_id])
        if not rows:
            raise Exception("Property not found")

        row = rows[0]
        property = Property(row['id'], row['name'], row['description'], row['price'], row['available_from'], row['available_to'], row['owner_id'])

        # Check if the booking dates are within the property's available dates
        requested_from = datetime.strptime(booking.requested_from, '%Y-%m-%d').date()
        requested_to = datetime.strptime(booking.requested_to, '%Y-%m-%d').date()
        if not (requested_from >= property.available_from and requested_to <= property.available_to):
            return False

        # Check for overlapping confirmed bookings
        bookings = self._connection.execute('''
            SELECT * FROM bookings
            WHERE property_id = %s
              AND is_confirmed = TRUE
              AND requested_to >= %s
              AND requested_from <= %s;
        ''', [booking.property_id, booking.requested_from, booking.requested_to])

        if bookings:
            return False
        
        return True