import sys
import random
import re

def matrix_input_size():
    while True:
        input_text = input("\nRindu skaits: ")
        if input_text.isdigit() and int(input_text) != 0:
            rows = int(input_text)
            break
        else:
            print("Ievades kļūda! Lūdzu ievadiet naturālu skaitli!".upper())
    while True:
        input_text = input("\nKolonu skaits: ")
        if input_text.isdigit() and int(input_text) != 0:
            columns = int(input_text)
            break
        else:
            print("Ievades kļūda! Lūdzu ievadiet naturālu skaitli!".upper())
    
    return rows, columns

def create_matrix(rows, columns):
    regex = '^[-+]?[0-9]*\.?[0-9]+$'
    print("\nIevadiet matricas vērtības:")
    matrix = [[None for j in range(columns)] for i in range(rows)]
    for row in range(rows):
        for column in range(columns):
            while True:
                input_text = input("[" + str(row) + "] [" + str(column) + "]: ")
                if re.match(regex, input_text):
                    matrix[row][column] = float(input_text)
                    break
                else:
                    print("Ievades kļūda! Lūdzu ievadiet reālu skaitli!".upper())
    return matrix

def random_matrix():
    return [[random.uniform(-50,50) for j in range(10)] for i in range(10)]
    
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            #print(element)
            print("{:<10.2f}".format(element), end='')
        print()


def reverse_odd_rows(matrix):
    for row in range(1,len(matrix),2):
        row_length = len(matrix[row]) 
        for element in range(0, int(row_length/2)):
            temp = matrix[row][element]
            matrix[row][element] = matrix[row][row_length - 1 - element]
            matrix[row][row_length - 1 - element] = temp
    
def swap_rows(matrix):
    for row in range(0, len(matrix)-1, 2):
        temp = matrix[row]
        matrix[row] = matrix[row + 1]
        matrix[row + 1] = temp
  
def main():

    if len(sys.argv) > 1 and sys.argv[1] == '-rand':
        matrix = random_matrix()
    else:
        rows, columns = matrix_input_size()
        matrix = create_matrix(rows, columns)


    print("\nMatrica pirms pārveidošanas: ")
    print_matrix(matrix)
    
    reverse_odd_rows(matrix)
    
    swap_rows(matrix)
    
    print("\nMatrica pēc pārveidošanas: ")
    print_matrix(matrix)

main()
