from room_nur import Room

import numpy as np


class Booking:
    def __init__(self, room, start_date, end_date):
        self.room = room
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Бронирование номера: {self.room.room_number}  ({self.room.room_type}) c {self.start_date} до {self.end_date}"
