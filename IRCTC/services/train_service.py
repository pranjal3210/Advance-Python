from models.train import Train


class TrainService:

    def __init__(self):

        self.trains = []

        self.add_train(
            Train(
                12301,
                "Rajdhani Express",
                "Delhi",
                "Mumbai",
                100
            )
        )

        self.add_train(
            Train(
                12951,
                "Mumbai Rajdhani",
                "Mumbai",
                "Delhi",
                100
            )
        )

        self.add_train(
            Train(
                12002,
                "Shatabdi Express",
                "Delhi",
                "Bhopal",
                80
            )
        )

    def add_train(self, train):
        self.trains.append(train)

    def show_all_trains(self):

        for train in self.trains:
            train.show_train()

    def search_trains(self, source, destination):

        results = []

        for train in self.trains:

            if (
                train.source.lower() == source.lower()
                and
                train.destination.lower() == destination.lower()
            ):
                results.append(train)

        return results