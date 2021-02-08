import sys

inLines = []
with open(sys.argv[1], 'r') as reader:
    inLines = reader.readlines()

for rawLine in inLines:
    line = rawLine.replace("\n", "")
    print(len(line))
