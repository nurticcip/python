class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.is_occupied = False
        self.price_per_night = price_per_night

    def __str__(self):
        return f"Комната: {self.room_number} ({self.room_type}):{'Занято'if self.is_occypied else 'Свободная'}, Цуна за Ночь:{self.price_per_night:.2f}"

    def check_availability(self):
        return not self.is_occupied

    def book_room(self):
        if not self.is_occupied:
            self.is_occupied = True
            return True
        else:
            return False

    def check_out(self):
        if not self.is_occupied:
            self.is_occupied = False
            return True
        else:
            return False
