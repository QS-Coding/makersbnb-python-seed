class Booking():
    def __init__(self, id, property_id, user_id, requested_from, requested_to, is_confirmed, total_price, created_at) -> None:
        self.id = id
        self.property_id = property_id
        self.user_id = user_id
        self.requested_from = requested_from
        self.requested_to = requested_to
        self.is_confirmed = is_confirmed
        self.created_at = created_at
        self.total_price = total_price
    
    def __repr__(self) -> str:
        return f'Booking({self.id}, {self.property_id}, {self.user_id}, {self.requested_from}, {self.requested_to}, {self.is_confirmed}, {self.total_price:.2f}, {self.created_at})'
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__