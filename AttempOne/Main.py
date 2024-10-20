
import random


def sectionLine() :
    print("--------------------------------------------")

print("Starting AttemptOne Main.py")

sectionLine()

print("Goal: a simple mx+y solver where a+y are static and the ai has to learn what m and y are, Allowing it to gennerate anything for a given x")

sectionLine()

print("Setting test scenario constants")

### Should not be used beyond comparison
correctM = 2
correctY = 1

def correctSolution(x) :
    return correctM * x + correctY

print("Generate test scenario")

testScenarios = []

for i in range(0, 100) :
    testScenarios.append([i, correctSolution(i)])

print("Test scenario generated length: " + str(len(testScenarios)))

sectionLine()

print("AI 'Training'")

def guessM(minvalue, maxvalue) :
    return random.randint(minvalue, maxvalue)
def guessY(minvalue, maxvalue) :
    return random.randint(minvalue, maxvalue)


iterationCount = 0
def trainAI(minvalueM, maxvalueM, minvalueY, maxvalueY) :
    global iterationCount
    iterationCount += 1
    print("Training iteration: " + str(iterationCount))

    nodes = []
    for i in range(0, 100) :
        m = guessM(minvalueM, maxvalueM)
        y = guessY(minvalueY, maxvalueY)
        nodes.append([m, y])

    for node in nodes :
        print("Node: " + str(node))
        errors = 0

        for scenario in testScenarios :
            x = scenario[0]
            a = scenario[1]
            guess = node[0] * x + node[1]
            error = abs(guess - a)
            if error == 0 :
                return
            else :
              errors += error
        print("Error: " + str(errors))
            
    


    
trainAI(-10, 10, -10, 10)