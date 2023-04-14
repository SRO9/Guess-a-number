import random as rnd


class Numbers:
    def __init__(self, number, try_num=0, counter=0):
        self.number = number
        self.try_num = try_num
        self.counter = counter

    def correct(self):
        while self.number != self.try_num:
            self.try_num = int(input("Try to guess number: "))
            if self.number > self.try_num:
                print(f"Wrong, number is bigger, try it again\n")
                self.counter += 1
            else:
                print(f"Wrong, number is lower, try it again\n")
                self.counter += 1

        return f"<<<Congrats!>>>, number is # {self.number} #\n{self.count_attempts()}"

    def count_attempts(self):
        return f"Number of attempts: {self.counter}"


num = Numbers(rnd.randint(1, 100))
print(num.correct())
