class Ticket:

    def __init__(self, user, train, seat_number, fare, pnr):
        self.user = user
        self.train = train
        self.seat_number = seat_number
        self.fare = fare
        self.pnr = pnr

    def show_ticket(self):
        print("\n========== TICKET ==========")
        print("PNR:", self.pnr)
        print("Passenger:", self.user.name)
        print("Train:", self.train.name)
        print("Train Number:", self.train.train_number)
        print("From:", self.train.source)
        print("To:", self.train.destination)
        print("Seat:", self.seat_number)
        print("Fare:", self.fare)
        print("============================")