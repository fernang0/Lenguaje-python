import numpy as np
#matriz random con dimension 3x3
matriz1 = np.random.randint(1,10,(3,3));
matriz2 = np.random.randint(1,10,(3,3));
print("Matriz 1: \n", matriz1);
print("Matriz 2: \n", matriz2);
#suma de matrices
suma = matriz1 + matriz2;
print("Suma de las matrices: \n", suma)
print(np.sum(matriz1))
