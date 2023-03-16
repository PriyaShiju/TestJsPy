class Flight:

    def __init__(self,number, aircraft):
        if not number[:2].isalpha():   #first 2 letters
            raise ValueError(f"No Airline code should start with numbers '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Airline code should start with capital letters '{number}'")

        if not(number[2:].isdigit() and int(number[2:]) <=9999 ): #last 2 letters
            raise ValueError(f"Invalid route number code '{number}' ")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [ {letter : None for letter in seats} for _ in rows]
  
    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

""" 
from airtravel import *
f=Flight("BA345",Aircraft("G-EUPT","Airbus345",22,6))
f._aircraft.seating_plan()
f._seating
""" 

class Aircraft:
    def __init__(self, registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows=num_rows
        self._num_seats_per_row = num_seats_per_row

    def seating_plan(self):
        return (range(1,self._num_rows+1),"ABCDEF")   #"ABCDEFGHJK"[:self._num_seats_per_row])

    def registration(self):
        return self._registration

    def model(self):
        return self._model

