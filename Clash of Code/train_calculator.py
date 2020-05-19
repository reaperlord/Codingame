n = int(input())
income =0
currentPassengers = 0

p, t = [int(i) for i in input().split()]
for i in range(n):
    d, u = [int(j) for j in input().split()]
    income += currentPassengers*p
    currentPassengers = currentPassengers - d + u

expense = t*n

print("%d %d %d"% (income,expense, 1 if income>expense else 0))