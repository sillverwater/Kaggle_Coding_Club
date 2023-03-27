import random

class Dice:
    def __init__(self):
        self.number = 0

    def getNumber(self):
        return self.number

    def roll(self):
        self.number = random.randint(1, 6)
        return self.number

class DiceProbability:
    def __init__(self, n):
        self.n = n
        self.b = [0, 0, 0, 0, 0, 0] #주사위 숫자가 나오는 확률
        self.a = [0] * n #N번의 주사위 숫자를 저장

    def calcProbability(self):
        for i in range(self.n):
            self.a[i] = Dice().roll()

        for i in range(6):
            self.b[i] = self.a.count(i+1) / len(self.a)

    def printProbability(self):
        for i in range(6):
            print(f"주사위 {i+1}: {self.a.count(i+1)} 비율: {self.b[i]}")

