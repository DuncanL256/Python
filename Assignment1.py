# Problem 1 (loops and arrays): create and initialize 2 n*n matrices of integers, calculate their product (standard matrix multiplication). 
# Hint: you will obtain an n*n matric as result, and usually you need 3 nested loops.

# Problem 2  (input/output/string): Read a list of family names (characters) until the user asks to stop (for example when entering a special character). 
# Print, lexicographically, the smallest name, the highest name, and the last name. Do not use any data structure to store the names (when possible)

n = 2

matrix_a = [[1, 2], [3, 4]] # Create the 2 matricies
matrix_b = [[5, 6], [7, 8]]

result = [[0 for _ in range(n)] for _ in range(n)] # Initialize the result matrix

# Perform matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

print("Resulting Matrix: ") # Print the result
for row in result:
    print(row)