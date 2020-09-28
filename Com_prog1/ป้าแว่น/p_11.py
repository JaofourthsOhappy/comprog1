def print_map(map):
    """
    Display 2D array by replacing 0 with ., 1 with #, and 2 with X
    :params 2D array contains integer 0,1,2
    :return nothing

    >>> print_map([[1,0],[0,2]])
    #.
    .X
    >>> print_map([[2,2,1],[0,0,0],[1,2,0]])
    XX#
    ...
    #X.
    >>> print_map([[0],[1],[2]])
    .
    #
    X
    """
    for row in map:
        for col in row:
            if col == 0 :
                print("." , end = '')
            elif col == 1 :
                print("#" , end = '')
            elif col == 2 :
                print("X" , end='')
        print()

map1 = [[1, 1, 1, 1],
               [1, 0, 0, 0],
              [1, 0, 1, 1],
                [0, 2, 0, 1],
                [1, 1, 0, 1]]

map2 = [[1, 1, 1, 1, 0, 0, 0, 1],
              [0, 2, 0, 0, 0, 1, 0, 1],
              [1, 1, 0, 1, 1, 0, 2, 1]]
#?
# print("Map 1")
# print_map(map1)
# print()
# print("Map 2")
# print_map(map2)
# print()


def read_matrix():
    """
    Read number of rows and columns of a matrix.
    Then, read each element and store it in a matrix.
    Return the read-in matrix
    :params Nothing
    :return 2D-list contains the matrix
    """
    row = int(input("Input #rows? "))
    col = int(input("Input #columns? "))
    matrix = []
    list_ =[]
    for i in range(1,row+1):
        for j in range(1,col+1):
            x = input(f"Input element[{i}][{j}]: ")
            list_.append(x)
        matrix.append(list_)
        list_ =[]
    return matrix
def print_matrix(matrix):
    """
    Display a matrix, where each number is displayed in 5 spaces and right-aligned.
    :params a 2D-list contains a matrix
    :return Nothing
    """
    count =0
    for i in matrix:
        for j in matrix[count]:
            print(f"{j:>5}" , end = "")
        print()
        count +=1

def transpose_matrix(matrix):
    """
    Transpose a matrix
    :params 2D-list contains an original matrix
    :return another 2D-list contains the transpose of original matrix

    >>> print_matrix(transpose_matrix([[1,2],[3,4]]))
        1    3
        2    4
    >>> print_matrix(transpose_matrix([[5,6,7],[8,9,10]]))
        5    8
        6    9
        7   10
    """
    list_ = []
    new_matrix = []
    for i in range(len(matrix[0])):
        for j in  range(len(matrix)):
            list_.append(matrix[j][i])
        new_matrix.append(list_)
        list_ = []
    return new_matrix
def print_row(matrix):
    """
    Print specific row from a matrix
    :params 2D-list contains an original matrix
    :return Nothing
        """
    num_row = int(input("Input row number: "))
    for i in matrix[num_row-1]:
        print(f"{i:>5}", end = '')
def print_column(matrix):
    """
    Print specific column from a matrix
    :params 2D-list contains an original matrix
    :return Nothing
    """
    num_col = int(input("Input column number: "))
    for i in matrix:
            print(f"{i[num_col-1]:>5}", end = '')
#? 5   8
#? 6   9
#? 7   10


# matrix = read_matrix()
# print("Matrix A is")
# print_matrix(matrix)
# option = input("Print row(r) or column(c)? ")
# if option == "r":
#     print_row(matrix)
# elif option == 'c' :
#     print_column(matrix)


n = int(input("Input n: "))
matrix = []
sum_tl_to_br = 0
sum_tr_to_bl = 0
for i in range(1,n+1):
    list_ = []
    for j in range(1,n+1):
        r =input(f"Input element[{i}][{j}]: ")
        list_.append(r)
    matrix.append(list_)
for i in range(len(matrix)):
    for j in  range(len(matrix[0])):
        if i ==j :
            sum_tl_to_br += int(matrix[i][j])
        elif  i-j ==2 or i-j ==-2 or  i and j == 0 :
            print(matrix[i][j] , end = ' ')
            # sum_tr_to_bl += int(matrix[i][j])

# print(sum_tl_to_br)
# print(sum_tr_to_bl)