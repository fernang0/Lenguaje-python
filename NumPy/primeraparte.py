import numpy as np
#array de una dimension
a1 = np.array([1,2,3]);
print(a1);
print();
a2 = np.array([[1,2,3], [4,5,6]]);
print(a2);
print();
a3 = np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(a3);
print("\n\n")
#crear un array con ciertos dimensiones
#crea un array con cierta dimension pero solo con 0
print(np.zeros((3,3)));
#cre un array con cierta dimension pero solo con 1
print(np.ones((3,2)));
#crear un array con cierta dimension pero con un valor especifico que se le de
print(np.full((3,3), 10));
#crea una referencia de matriz con dimension n
print(np.identity(3));
#crea un array con inicio, fin y paso
print(np.arange(1,4,1));
#random
print ("\n\n")
print(np.random.random((3,3)));