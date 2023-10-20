def is_odd(num):
    return num % 2 != 0

def calculate_expected_sum(n):
    return (n ** 2 * (n ** 2 + 1)) // (2 * n)

def generate_magic_square(n, start_num, step):
    magic_square = [[0] * n for _ in range(n)]
    
    i, j = 0, n // 2
    
    for _ in range(n * n):
        magic_square[i][j] = start_num
        start_num += step
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j] == 0:
            i, j = new_i, new_j
        else:
            i = (i + 1) % n
    
    return magic_square

def print_magic_square(square):
    print('+' + '---+' * len(square[0]))
    for row in square:
        for num in row:
            print('|{:3d}'.format(num), end=' ')
        print('|')
        print('+' + '---+' * len(square[0]))

while True:
    n = int(input("Enter the order of the magic square (odd number): "))
    if is_odd(n):
        break
    else:
        print("Please enter an odd number for the order.")

while True:
    start_num = int(input("Enter the starting number: "))
    if start_num >= 0:
        break
    else:
        print("Please enter a non-negative starting number.")

while True:
    step = int(input("Enter the step: "))
    if step > 0:
        break
    else:
        print("Please enter a positive step.")

expected_sum = calculate_expected_sum(n)
print("Expected sum of the numbers in the magic square:", expected_sum)

magic_square = generate_magic_square(n, start_num, step)
print('Magic Square of order', n)
print_magic_square(magic_square)
