start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))

squares = []
even_squares = []
odd_squares = []

for i in range(start, end + 1):
    square = i ** 2
    squares.append((i, square)) 
    
    if square % 2 == 0:
        even_squares.append((i, square))
    else:  
        odd_squares.append((i, square))   

print("squares (number, square):")
for num, square in squares:
    print(str(num) + ": " + str(square))

print("\nEven Squares (number, square):")
for num, square in even_squares:
    print(str(num) + ": " + str(square))

print("\nOdd Squares (number, square):")
for num, square in odd_squares:
    print(str(num) + ": " + str(square))
