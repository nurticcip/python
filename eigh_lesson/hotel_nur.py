import numpy as np
import pandas as pd

from booking_nur import Booking


class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_number):
        room_to_remove = self.find_room(room_number)
        if room_to_remove:
            self.rooms.remove(room_to_remove)

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def create_booking(self, room_number, start_date, end_date):
        room = self.find_room(room_number)
        if room and room.check_availability():
            booking = Booking(room, start_date, end_date)
            self.bookings.append(booking)
            room.book_room()
            return booking
        else:
            return None

    def generate_report(self):
        room_data = {
            "Номер Комнаты:": [room.room_number for room in self.rooms],
            "Катигория Комнаты:": [room.room_type for room in self.rooms],
            "Цена за сутки:": [room.price_per_night for room in self.rooms],
            "Забронировано:": [room.is_occupied for room in self.rooms],
        }

        booking_data = {
            "Номер Комнаты:": [booking.room.room_number for booking in self.bookings],
            "Дата заселения:": [booking.start_date for booking in self.bookings],
            "Дата высиления:": [booking.end_date for booking in self.bookings],
        }
        room_df = pd.DataFrame(room_data)
        booking_df = pd.DataFrame(booking_data)

        report = f"Отуль: {self.hotel_name}"
        report += "Комнаты: 30\n"
        report += room_df.to_string(index=False) + "\n"
        report += "Заказы: 10 \n"
        report += booking_df.to_string(index=False) + "\n"
        return report
