from lib.models.booking import *

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
        self._connection.execute("INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) VALUES (%s, %s, %s, %s, %s, %s)", [booking.property_id, booking.user_id, booking.requested_from, booking.requested_to, booking.total_price, booking.created_at])
    
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