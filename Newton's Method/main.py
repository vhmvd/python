import pandas as pd

def newton_interpolation(xVar, yVar, xi):
    # Number of datapoints
    lengthOfDatapoints = len(xVar)
    # Divided difference init
    dividedDifference = [[None for x in range(lengthOfDatapoints)] for x in range(lengthOfDatapoints)]
    #f(X) values at different degrees
    valuesAtDiffDeg = [None for x in range(lengthOfDatapoints)]

    errorValue = [None for x in range(lengthOfDatapoints)]
    
    # Finding the divided difference
    for i in range(lengthOfDatapoints):
        dividedDifference[i][0] = yVar[i]
    for j in range(1,lengthOfDatapoints):
        for i in range(lengthOfDatapoints-j):
            dividedDifference[i][j] = (dividedDifference[i+1][j-1] - dividedDifference[i][j-1])/(xVar[i+j]-xVar[i])
    
    # Printing the divided difference
    dividedDiffTable = pd.DataFrame(dividedDifference)
    print(dividedDiffTable)
    
    # Interpolating xi
    xterm = 1
    valuesAtDiffDeg[0] = dividedDifference[0][0]
    for var in range(1, lengthOfDatapoints):
        xterm = xterm * (xi - xVar[var-1])
        valuesAtdiffDeg2 = valuesAtDiffDeg[var-1] + dividedDifference[0][var]*xterm
        errorValue[var-1] = valuesAtdiffDeg2 - valuesAtDiffDeg[var-1]
        valuesAtDiffDeg[var] = valuesAtdiffDeg2
    # Returns the map for pandas dataframe
    return map(lambda yy, ee : [yy, ee], valuesAtDiffDeg, errorValue)


# Sample data
x = [1, 4, 6, 5.1, 2.8, 1.4, 2.1, 3.2]
y = [0, 1.3862944, 1.7917595, 1.6094379, 1.0986123 , 0.4054641, 0.9162907, 1.2527630]

a = newton_interpolation(x, y, 2)
df = pd.DataFrame(a, columns=['f(x)', 'error'])