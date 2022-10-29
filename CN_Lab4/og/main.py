from os import sep
from pydoc import doc
from re import X
import numpy as np
import copy
from time import perf_counter

epsilon = 10 ** (-4)


def parse_input(text):
    words =text.split(',') 
    value = float(words[0]) 
    i = int(words[1]) 
    j = int(words[2]) 
    return (value, i , j) 


def read_matrix_from(path):
    with open(path,encoding='utf8', newline='\r\n') as fd:
        count = fd.readline()
        output_vector = [[] for i in range(int(count))]

        fd.readline() # there is a white space
        
        while True:
            line = fd.readline()
            if not line:
                break

            # print(line)
            value, i, j = parse_input(line)
            found = 0
            for vec in output_vector[i]: 
                if vec[1] == j:
                    vec[0] += value
                    found = 1
                    break
            if found == 0 :
                output_vector[i].append([value,j]) 

            if j > i :
                print("invalid format") 
                break
        return output_vector, int(count)


def read_results_from(path):
     with open(path,encoding='utf8', newline='\r\n') as fd:
        output_vector = []

        while True:
            line = fd.readline()
            if not line:
                break

            output_vector.append(float(line))

        return output_vector


def get_element(matrix, i, j):
    for col in matrix[i]:
        if col[1] == j:
            return col[0]
    return 0
  

def compute_delta(x_c, x_p):
    x_c = np.array(x_c)
    x_p = np.array(x_p)  
    return np.linalg.norm(x_c - x_p)


def diagonala(A, count):
    result = []
    for i in range(count):
        for j in A[i]:
            if j[1] == i:
                result.append(j[0])

    return result

    
def memoizare_linii(a, count):
    result = []
    
    for line in range(count):
        curr_dict = dict()
        for element in a[line]: 
            # print(element[0], element[1])
            curr_dict.update({element[1]: element[0]})
            # print(f"{element[1]} : {element[0]}")
       
        for i in range(line + 1, count):
            # ce element se afla pe coloana line
            for j in a[i]:
                if j[1] == line:
                    curr_dict.update({i: j[0]})
                    # print(f"{i} : {j[0]}")
        
        result.append(curr_dict)
    # print(result[4])
    return result


def metoda_iterativa_rezolvare_sistem(A, B, count):
    x_c = [0 for x in range(count)]
    d = diagonala(A, count)

    start = perf_counter()

    vectori = memoizare_linii(A, count)

    stop = perf_counter()
    print(f'Timp trecut = {stop - start}')

    k = 0
    k_max = 1000
    delta_max = 10 ** 8

    start = perf_counter()

    while True:
        x_p = copy.deepcopy(x_c)

        # calculam x_c in functie de x_p
        for i in range(count):

            sum = B[i]

            for j in vectori[i].keys():   
                if j == i:
                    continue       
                sum -= x_p[j] * vectori[i][j]
                # print(f"x_j = {x_p[j]} --- i = {i} j = {j} a_i_j = {get_element(A,i,j)}")

            # sum = B[i] 
            # for j in range(0, i):          
            #     sum -= x_p[j] * get_element(A,i,j)
            #     # print(f"x_j = {x_p[j]} --- i = {i} j = {j} a_i_j = {get_element(A,i,j)}")
                
            # for j in range(i + 1, count):
            #     sum -= x_p[j] * get_element(A,j,i)
            #     # print(f"x_j = {x_p[j]} --- i = {i} j = {j} a_i_j = {get_element(A,i,j)}")
                
            sum = sum / d[i]
            x_c[i] = sum

        # print(x_c)

        delta_x = compute_delta(x_c, x_p)  

        print(f'Delta = {delta_x}', flush=True)
        print(k)
        # stop = perf_counter()
        # print(f'Timp trecut = {stop - start}')

        k += 1
        if delta_x  < epsilon or k > k_max or delta_x > delta_max:
            break

    if delta_x < epsilon:
        print("e bn")
        print(x_c) 
    else:
        print("nu-i bn")

    stop = perf_counter()
    print(f'Timp trecut = {stop - start}')

     
def main():
    # array_test, count_test = read_matrix_from('a.txt')
    # array_b = read_results_from('b.txt')

    # metoda_iterativa_rezolvare_sistem(array_test, array_b, count_test)

    array_test, count_test = read_matrix_from('a_1.txt')
    array_b = read_results_from('b_1.txt')

    metoda_iterativa_rezolvare_sistem(array_test, array_b, count_test)



main()