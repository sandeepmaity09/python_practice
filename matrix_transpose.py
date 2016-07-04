#!/usr/bin/python3

# Program for matrix transpose

matrix=[[1,2,3,4,13],[5,6,7,8,14],[9,10,11,12,15]]
print(matrix)


transpose=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

# a more readable code

transposed=list()
for i in range(len(matrix[0])):
	transposed_row=list()
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)
print(transposed)


# a another way to transpose
trans=list()
for i in range(len(matrix[0])):
	trans.append([row[i] for row in matrix])

print(trans)

# by using a built-in function

print(list(zip(*matrix)))
