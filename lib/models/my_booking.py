from datetime import date

class MyBooking:
    
    def __init__(self, property_name, owner_id, requested_by, request_id, is_confirmed, total_price, requested_from, requested_to) -> None:
        self.property_name = property_name
        self.request_id = request_id
        self.owner_id = owner_id
        self.requested_by = requested_by
        self.is_confirmed = is_confirmed
        self.total_price = total_price
        self.requested_from = requested_from
        self.requested_to = requested_to

    def __repr__(self) -> str:
        return f"MyBooking({self.property_name}, {self.owner_id}, {self.requested_by}, {self.request_id}, {self.is_confirmed}, {self.total_price}, {self.requested_from}, {self.requested_to})"
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__