from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        x = 100
        time = 0
        while x > 0:
            x -= self.power
            time += 1
            print(f'{self.name}, сражается {time} дней, осталось {x} воинов')
            sleep(1)
        print(f'{self.name} одержал победу спустя {time} дней!')


knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()
print('Все битвы закончились!')
