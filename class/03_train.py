'''
1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats, seatNo):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.seatNo = seatNo
    l1 = [1,2,3,4,5,6,7,8,9,10]
    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        print(f"your seatno is {self.seatNo} is cancled")
        self.seats = self.seats + 1


intercity = Train("Intercity Express: 14015", 90, 10 , 8)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTicket(8)
intercity.getStatus()
