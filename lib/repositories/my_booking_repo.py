from lib.models.my_booking import *

class MyBookingRepo:
    
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all_my_bookings(self, user_id):
        rows = self._connection.execute('''
select properties."name" as property_name, properties.owner_id, users."name" as requested_by, bookings.id as request_id, bookings.is_confirmed, bookings.total_price, bookings.requested_from, bookings.requested_to, bookings.created_at from bookings
join properties on bookings.property_id=properties.id
join users on bookings.user_id=users.id
where users.id=%s;
                                ''', [user_id])
        my_bookings = []
        for row in rows:
            my_booking = MyBooking(row['property_name'], row['owner_id'], row['requested_by'], row['request_id'], row['is_confirmed'], row['total_price'], row['requested_from'], row['requested_to'], row['created_at'])
            my_bookings.append(my_booking)
        return my_bookings
    
    def all_my_property_bookings(self, user_id):
        rows = self._connection.execute('''
select properties."name" as property_name, properties.owner_id, users."name" as requested_by, bookings.id as request_id, bookings.is_confirmed, bookings.total_price, bookings.requested_from, bookings.requested_to, bookings.created_at from bookings
join properties on bookings.property_id=properties.id
join users on bookings.user_id=users.id
where properties.owner_id=%s;
                                ''', [user_id])
        my_bookings = []
        for row in rows:
            my_booking = MyBooking(row['property_name'], row['owner_id'], row['requested_by'], row['request_id'], row['is_confirmed'], row['total_price'], row['requested_from'], row['requested_to'], row['created_at'])
            my_bookings.append(my_booking)
        return my_bookings