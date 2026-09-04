# Run with this: python3 src/PythonBasics/exercise-02.py
# or Copy path reference - content root

# section::section-8::start
# 08 Solid Square / Rectangle (not recommended)
def print_solid_square_rectangle():
    n = 5
    for x in range(0,n):
        print(" * " * n)

# Solid Square / Rectangle
def print_solid_square_rectangle_v2():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            print("*", end=" ")
# section::section-8::end

# 09 Hollow Square / Rectangle
# section::section-9::start
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
# section::section-9::end

# 10 Left-Aligned Right Triangle
# section::section-10::start
def print_left_aligned_right_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,i):
                print("*", end=" ")
# section::section-10::end

# 11 Inverted Left-Aligned Triangle
# section::section-11::start
def print_inverted_left_aligned_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n-i):
            print("*", end=" ")
# section::section-11::end

# 12 Mirrored (Right-Aligned) Right Triangle
# section::section-12::start
def print_mirrored_right_aligned_right_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            if j < n-i  :
                print(" ", end=" ")
            else:
                print("*", end=" ")
# section::section-12::end


# 00 Right-Aligned Left Triangle
# section::section-00::start
def print_right_aligned_left_triangle():
    n = 5
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            if i > j:
                print(" ", end=" ")
            else:
                print("*", end=" ")
# section::section-00::end


# 13. Full Equilateral Pyramid
# section::section-13::start
def print_full_equilateral_pyramid(n: int):
    midIndex = (n-1)/2
    for i in range(0,n):
        print("", end="\n")
        for j in range(0,n):
            if (midIndex - i) <= j <= (midIndex + i): # if j == midIndex:
                print("*", end="")
            else:
                print(" ", end="")
# section::section-13::end



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
print('\n------------------')
print_full_equilateral_pyramid(7) # even
print_full_equilateral_pyramid(8) # odd
