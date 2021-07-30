
def printArraystring(string, n):
	for i in range(n):
		print(string[i], end = " ")


def sort(s, n):
	for i in range(1, n):
		temp = s[i]

		j = i - 1
		while j >= 0 and len(temp) < len(s[j]):
			s[j + 1] = s[j]
			j -= 1

		s[j + 1] = temp
if __name__ == "__main__":
    n1=int(input())
    if n1>0:
        arr=[]
        for i in range(n1):
            x=input()
            arr.append(x)
	
	    n = len(arr)

	
	    sort(arr, n)


	
	    printArraystring(arr, n)
    else:
        print("invalid input")


