import pickle

fileToRead = input("Enter file name to be used: ")
instances = pickle.load(open(fileToRead, 'rb'))
nList = instances["n_list"]
xList = instances["x_list"]
yList = instances["y_list"]
CList = instances["C_list"]

sumX = []
sumY = []
sumXSquare = []
sumYSquare = []
sumProduct = [] 
bestCost = []
bestPoints = []
k_list = []
last_points_list = []
OPT_list = []
finalSolution = []

        
        
def CalcError(i, j):    
      n = j-i+1
      intX = sumX[j+1] - sumX[i]
      intY = sumY[j+1] - sumY[i]
      intXSquare = sumXSquare[j+1] - sumXSquare[i]
      intYSquare = sumYSquare[j+1] - sumYSquare[i]
      intProduct = sumProduct[j+1] - sumProduct[i]
      ErrA = ((n*intProduct) - (intX * intY)) 
      if ((n*intXSquare) - pow(intX, 2)) == 0:
          ErrA = float('inf')
          return float('inf')
      else:
          ErrA = ErrA / ((n*intXSquare) - pow(intX, 2))
      ErrB = (intY - (ErrA * intX)) / n
      err =  (intYSquare - (ErrA*2*intProduct) - (2*ErrB*intY) + (2*ErrB*ErrA*intX) + n*pow(ErrB,2) + (pow(ErrA,2)*intXSquare))
      return err

for a in range(len(nList)):
    sumX = [0] * (len(xList[a]))
    finalSum = [0] * (len(xList[a]))
    sumY = [0] * (len(xList[a]))
    sumXSquare = [0] * (len(xList[a]))
    sumYSquare = [0] * (len(xList[a]))
    sumProduct = [0] * (len(xList[a])) 
    bestCost = [0] * (len(xList[a]))
    bestPoints = [0] * (len(xList[a]))
    for i in range(0,nList[a]):
        sumX[i] = sumX[i-1] + xList[a][i]
        sumY[i] = sumY[i-1] + yList[a][i]
        sumXSquare[i] = sumXSquare[i-1] + pow(xList[a][i], 2)
        sumYSquare[i] = sumYSquare[i-1] + pow(yList[a][i], 2)
        sumProduct[i] = sumProduct[i-1] + (xList[a][i] * yList[a][i])
    sumX.insert(0,0)
    sumY.insert(0,0)
    sumXSquare.insert(0,0)
    sumYSquare.insert(0,0)
    sumProduct.insert(0,0)
    for j in range(0,nList[a]):
        k = 0
        l = float('inf')
        for i in range(0, j):
            q = CalcError(i, j) + bestCost[i-1]
            if q < l:
                l = q
                k = i
        bestCost[j] = l + CList[a]
        bestPoints[j] = k
    i = nList[a]-1
    temp = bestPoints[nList[a]-1]
    tempLast = []
    k = 0
    while i > 0:
        tempLast.insert(0,i)
        k = k + 1
        i = temp-1
        temp = bestPoints[i]
    k_list.append(k)
    last_points_list.append(tempLast)
    OPT_list.append(bestCost[len(bestCost)-1])

finalSolution = {
    "k_list" : k_list,
    "last_points_list" : last_points_list,
    "OPT_list" : OPT_list
}

pickle.dump(finalSolution, open("P2Solutions", 'wb'))
print("Solutions dumped into P2Solutions")