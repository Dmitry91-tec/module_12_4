import logging


class Runner:
    def __init__(self, name, speed=5):
        try:
            if isinstance(name, str):
                self.name = name
            else:
                raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
            logging.info('"test_run" выполнен успешно')
        except Exception:
            logging.exception("Неверный тип данных для объекта Runner", exc_info=True)
        try:
            self.distance = 0
            if speed > 0:
                self.speed = speed
            else:
                raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
            logging.info('"test_walk" выполнен успешно')
        except Exception:
            logging.error("Неверная скорость для Runner", exc_info=True)
    def run(self):
        self.distance += self.speed * 2
        return

    def walk(self):
        self.distance += self.speed
        return


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')


first = Runner("Den", 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())

