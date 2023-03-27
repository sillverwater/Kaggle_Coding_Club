from dice import DiceProbability

n = int(input("총 횟수: "))
dice = DiceProbability(n)
dice.calcProbability()
dice.printProbability()
