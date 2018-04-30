def fib():
    n = input("Enter the number of Fibonacci numbers you would like to generate (must be an integer: ")
    if(int(n) < 1):
	    while(int(n) < 1):
		    n = input("Your input was invalid, please try again: ")

    num = int(n)
    arr = []
    arr.append(0);
    if(num > 1):
    	arr.append(1)
    if(num > 2):
    	fibgen(arr, 0, 1, n)

    for i in arr:
     print i,


def fibgen(arr, first, second, length):
    if(len(arr) == length):
    	return
    num = arr[first] + arr[second]
    arr.append(num)
    fibgen(arr, first+1, second+1, length)


fib()