from models.ticket import Ticket


class BookingService:

    def __init__(self):
        self.tickets = []
        self.pnr_counter = 1000000000

    def book_ticket(self, user, train, fare):

        if train.available_seats <= 0:
            print("\nSorry! No seats available.")
            return None

        train.book_seat()

        seat_number = train.total_seats - train.available_seats

        self.pnr_counter += 1

        pnr = str(self.pnr_counter)

        ticket = Ticket(
            user,
            train,
            seat_number,
            fare,
            pnr
        )

        self.tickets.append(ticket)

        print("\nTicket booked successfully! 🎉")

        return ticket
    
    def get_user_tickets(self, user):

        user_tickets = []

        for ticket in self.tickets:

            if ticket.user == user:
                user_tickets.append(ticket)

        return user_tickets