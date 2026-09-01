from services.auth_service import AuthService
from services.train_service import TrainService
from services.booking_service import BookingService


class IRCTCApp:

    def __init__(self):
        self.auth_service = AuthService()
        self.train_service = TrainService()
        self.booking_service = BookingService()

        self.current_user = None

    # =========================
    # START APPLICATION
    # =========================

    def start(self):

        print("\n==============================")
        print("       WELCOME TO IRCTC")
        print("==============================")

        while True:

            print("\n1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "3":
                print("\nThank you for using IRCTC!")
                break

            else:
                print("\nInvalid choice. Please try again.")

    # =========================
    # REGISTER
    # =========================

    def register(self):

        self.auth_service.register()

    # =========================
    # LOGIN
    # =========================

    def login(self):

        user = self.auth_service.login()

        if user:
            self.current_user = user
            self.user_menu()

    # =========================
    # USER MENU
    # =========================

    def user_menu(self):

        while self.current_user:

            print("\n==============================")
            print(f"       WELCOME, {self.current_user.name}")
            print("==============================")

            print("1. Search Train")
            print("2. Book Ticket")
            print("3. My Tickets")
            print("4. Profile")
            print("5. Logout")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.search_train()

            elif choice == "2":
                self.book_ticket()

            elif choice == "3":
                self.show_tickets()

            elif choice == "4":
                self.current_user.show_profile()

            elif choice == "5":
                self.logout()

            else:
                print("\nInvalid choice. Please try again.")

    # =========================
    # SEARCH TRAIN
    # =========================

    def search_train(self):

        source = input("\nEnter source: ")
        destination = input("Enter destination: ")

        results = self.train_service.search_trains(
            source,
            destination
        )

        if not results:
            print("\nNo trains found.")
            return

        print("\n========== TRAINS ==========")

        for train in results:
            train.show_train()

    # =========================
    # BOOK TICKET
    # =========================

    def book_ticket(self):

        source = input("\nEnter source: ")
        destination = input("Enter destination: ")

        results = self.train_service.search_trains(
            source,
            destination
        )

        if not results:
            print("\nNo trains found.")
            return

        print("\n========== AVAILABLE TRAINS ==========")

        for index, train in enumerate(results, start=1):

            print(
                f"{index}. "
                f"{train.train_number} - "
                f"{train.name} - "
                f"Seats: {train.available_seats}"
            )

        try:
            choice = int(input("\nSelect train: "))

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        if choice < 1 or choice > len(results):
            print("\nInvalid train selection.")
            return

        selected_train = results[choice - 1]

        # Temporary fixed fare.
        # Later we will calculate this properly.
        fare = 1500

        ticket = self.booking_service.book_ticket(
            self.current_user,
            selected_train,
            fare
        )

        if ticket:
            ticket.show_ticket()

    # =========================
    # SHOW USER TICKETS
    # =========================

    def show_tickets(self):

        tickets = self.booking_service.get_user_tickets(
            self.current_user
        )

        if not tickets:
            print("\nYou have no tickets.")
            return

        print("\n========== MY TICKETS ==========")

        for ticket in tickets:
            ticket.show_ticket()

    # =========================
    # LOGOUT
    # =========================

    def logout(self):

        print(
            f"\nGoodbye, {self.current_user.name}!"
        )

        self.current_user = None