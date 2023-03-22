import random

class Dice:
    def __init__(self):
        self.number = self.roll()

    def getNumber(self):
        return self.number

    def roll(self):
        self.number = random.randint(1, 6)
        return self.number

class DiceProbability:
    def __init__(self, n):
        self.cnt = [0, 0, 0, 0, 0, 0] #주사위 숫자가 나온 횟수
        self.b = [0, 0, 0, 0, 0, 0] #주사위 숫자가 나오는 확률
        self.a = [Dice() for _ in range(n)] #N번의 주사위 숫자를 저장

    def calcProbability(self):
        for i in range(len(self.a)):
            k = self.a[i].getNumber()
            self.cnt[k - 1] += 1

        for i in range(6):
            self.b[i] = self.cnt[i] / len(self.a)

    def printProbability(self):
        for i in range(6):
            print(f"주사위 {i+1}: {self.cnt[i]} 비율: {self.b[i]}")