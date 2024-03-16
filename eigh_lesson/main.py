from room_nur import Room
from booking_nur import Booking
from hotel_nur import Hotel

# Добавление комнат

room1 = Room("11", "Стандарт", 500)
room2 = Room("12", "Люкс", 1000)
room3 = Room("13", "Стандарт", 800)


# Пример использования:
hotel = Hotel("nur: ")

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)


# Создание бронирования
booking1 = hotel.create_booking("11", "2023-09-07", "2023-09-15")
booking2 = hotel.create_booking("12", "2023-09-04", "2023-09-14")

if booking1:
    print(f"Бронирования прошло успушно: {booking1}")
else:
    print("Ошибка бронирвания.")

if booking2:
    print(f"Бронированиу пршло успушно: {booking2}")
else:
    print("Ошибка бронирвания.")

report = hotel.generate_report()
print(report)
