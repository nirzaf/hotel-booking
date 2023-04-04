"""
User can see the list of Hotels
User can book a Hotel
User can get a reservation ticket

Classes:
    Hotel
    ReservationTicket
    User

"""

import pandas as pd


class User:
    def view_hotels(self):
        pass


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book the hotel by changing the value of available column to No"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available or not"""
        if df.loc[df["id"] == self.hotel_id, "available"].item() == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"Dear {self.customer_name},\n\nThank you for booking with {self.hotel_object}"
        return content


df = pd.read_csv("hotels.csv", dtype={"id": str, "name": str, "available": str})

print(df)
hotel_Id = input("Enter the id of the hotel you want to book: ")
hotel = Hotel(hotel_Id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    hotel_name = df.loc[df["id"] == hotel_Id, "name"].item()
    reservation_ticket = ReservationTicket(name, hotel_name)
    print(reservation_ticket.generate())
else:
    print("Sorry, the hotel is not available.")
