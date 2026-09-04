# Run with this: python3 src/PythonBasics/exercise-02.py

# 08  Solid Square / Rectangle (not recommended)
def print_solid_square_rectangle():
    n = 4
    for x in range(0,n):
        print("*" * n)

# 08  Solid Square / Rectangle
def print_solid_square_rectangle_v2():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            print("*", end=" ")


# 09 Hollow Square / Rectangle
def print_hollow_square_rectangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            if i == 0 or i == n-1: # for 1st and last row, print all *
                print("*", end=" ")
            else:
                if j > 0 and j < n-1:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")

                """    
                if j == 0 or j == n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
                """

# 10 Left-Aligned Right Triangle
def print_left_aligned_right_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,i):
                print("*", end=" ")

# 11 Inverted Left-Aligned Triangle
def print_inverted_left_aligned_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n-i):
            print("*", end=" ")

# 12 Mirrored (Right-Aligned) Right Triangle
def print_mirrored_right_aligned_right_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            if j < n-i  :
                print(" ", end=" ")
            else:
                print("*", end=" ")


# 00 Right-Aligned Left Triangle
def print_right_aligned_left_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            if i > j:
                print(" ", end=" ")
            else:
                print("*", end=" ")





#======== main ========
print_solid_square_rectangle()
print('\n------------------')
print_solid_square_rectangle_v2()
print('\n------------------')
print_hollow_square_rectangle()
print('\n------------------')
print_left_aligned_right_triangle()
print('\n------------------')
print_inverted_left_aligned_triangle()
print('\n------------------')
print_mirrored_right_aligned_right_triangle()
print('\n------------------')
print_right_aligned_left_triangle()