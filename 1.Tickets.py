import array
import sys

def sumDigitsOf(number):
    actualNumber = number
    sumOfDigits = 0
    while actualNumber > 0:
        digit = actualNumber % 10
        sumOfDigits += digit
        actualNumber = int(actualNumber / 10)
    return int(sumOfDigits)

line = ""
with open(sys.argv[1]) as reader:
    line = reader.readline().replace("\n", "")
n = int(line)

nList = []
for value in range(0, n * 9 + 1):
	nList.append(0)
sums = array.array('i', nList)

for number in range(0, pow(10,n)):
    sumOfDigits = int(sumDigitsOf(number))
    prevSum = sums[sumOfDigits]
    sums[sumOfDigits] =  prevSum + 1
count = 0
for sum in sums:
    count += sum * sum
print(count)