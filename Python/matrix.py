#Test data
A = [[2.0, 4.0, 2.0], [2.0, 2.0, 6.0], [4.0, 2.0, 2.0]]
b = [3.0, 4.0, 5.0]


def gauss_elim(A, b):
    n = len(b)
    #i = 0
    for i in range(0,n-1):
    #while i < n-1:
        #If diagonal is zero
    	if A[i][i] == 0:
    		print("error")
    		return (None, None)
        #j = i+1
        #iterate through each row
        for j in range(i+1, n):
       #while j < n:
            #k = i
            b[j] = b[j] - (A[j][i] / A[i][i]) * b[i]
            t = (A[j][i] / A[i][i]) #Fraction by which each row is reduced
            #iterate through each column
            for k in range(i, n):
            #while k < n:
                A[j][k] = A[j][k] - ((t) * A[i][k])
                #k += 1
            #j += 1
        #i += 1
    return (A, b)

def back_sub(A, b):
    n = len(b)
    x = range(0,n)
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += (A[i][j])*x[j]
        x[i] = (b[i] - sum) / A[i][i]

    return x

(A, b) = gauss_elim(A, b)
if A != None and b != None:
    x = back_sub(A, b)
    print("Result is ")
    for val in x:
        print(val)
else:
    print("Something went wrong")
