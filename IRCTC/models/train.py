class Train:
    
    def __init__(self,train_number,name,source,destination,total_seats):
        self.train_number = train_number
        self.name=name
        self.source=source
        self.destination=destination
        self.total_seats = total_seats
        self.available_seats = total_seats
        
    def show_train(self):
        print("\n---------- TRAIN ----------")
        print("Train Number:", self.train_number)
        print("Train Name:", self.name)
        print("From:", self.source)
        print("To:", self.destination)
        print("Available Seats:", self.available_seats)
        print("---------------------------")
        
        
    def book_seat(self):

        if self.available_seats > 0:
            self.available_seats -= 1
            return True

        return False