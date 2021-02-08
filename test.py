import sys
from enum import Enum, auto
import subprocess

args = {}
class ArgType(Enum):
    runFile = auto()
    inFile = auto()
    outFile = auto()
if len(sys.argv) != 4:
    print("Wrong parameters. Usage <file to run> <in result file> <out result file>")
    quit(1)
args[ArgType.runFile] = sys.argv[1]
args[ArgType.inFile] = sys.argv[2]
args[ArgType.outFile] = sys.argv[3]

command = args[ArgType.runFile] + " " + args[ArgType.inFile]
proc = subprocess.Popen("python3 " + command, stdout=subprocess.PIPE, shell = True)
encodedResult = proc.communicate()[0]
textResult = encodedResult.decode(encoding='utf-8')
resultLines = list(filter(lambda l: l != "", list(map(lambda s: s.replace("\n", ""), textResult.split("\n")))))
print(resultLines)
outLines = []
with open(args[ArgType.outFile], 'r') as outputReader:
    outLines = outputReader.readlines()
outLines = list(filter(lambda l: l != "", list(map(lambda s: s.replace("\n", ""), outLines))))
print(outLines)
testCorrect = True
if len(resultLines) == len(outLines):
    for lineIndex in range(0, len(outLines)):
        outLine = outLines[lineIndex]
        resultLine = resultLines[lineIndex]
        if outLine != resultLine:
            testCorrect = False
            break
else:
    testCorrect = False
print("Test result: " + ("PASSED" if testCorrect else "FAILED"))


