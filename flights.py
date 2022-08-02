class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(3)
person = ["Jackson","Ron","Hermoine","Harry"]
for people in person:
    if flight.add_passengers(people):
        print(f"{people} was succesfully add in the flight")
    else:
        print(f"Failed to added {people}")