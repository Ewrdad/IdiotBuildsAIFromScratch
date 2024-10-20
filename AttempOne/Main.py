
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
    for i in range(0, 10) :
        m = guessM(minvalueM, maxvalueM)
        y = guessY(minvalueY, maxvalueY)
        nodes.append([m, y])

    results = []
    for node in nodes :
        print("Node: " + str(node))
        errors = 0

        for scenario in testScenarios :
            x = scenario[0]
            a = scenario[1]
            guess = node[0] * x + node[1]
            error = guess - a
            errors += error
        print("Error: " + str(errors))
        results.append([node, errors])

    #find best 10 nodes based on error distance to 0
    results.sort(key=lambda x: abs(x[1]))
    bestNodes = results[:10]
    print("Best nodes: " + str(bestNodes))

    lowestErrors = bestNodes[0][1]

    # Define new min and max values for m and y
    listOfMValues = [node[0][0] for node in bestNodes]
    listOfYValues = [node[0][1] for node in bestNodes]

    newMinValueM = min(listOfMValues)
    newMaxValueM = max(listOfMValues)
    newMinValueY = min(listOfYValues)
    newMaxValueY = max(listOfYValues)

    print("New min and max values for m: " + str(newMinValueM) + " " + str(newMaxValueM))
    print("New min and max values for y: " + str(newMinValueY) + " " + str(newMaxValueY))
    return [newMinValueM, newMaxValueM, newMinValueY, newMaxValueY , lowestErrors]


minValueM = -10
maxValueM = 10
minValueY = -10
maxValueY = 10

while True :
    sectionLine()
    print("Training iteration: " + str(i))
    newValues = trainAI(minValueM, maxValueM, minValueY, maxValueY)
    minValueM = newValues[0]
    maxValueM = newValues[1]
    minValueY = newValues[2]
    maxValueY = newValues[3]
    print("Lowest errors: " + str(newValues[4]))
    if newValues[4] == 0 :
        print("Training complete")
        break
    sectionLine()

        
    


    
trainAI(-10, 10, -10, 10)