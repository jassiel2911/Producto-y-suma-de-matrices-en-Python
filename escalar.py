import numpy

r1=int(input("Numero de filas de M1: "))
c1=int(input("Numero de columnas de M1: "))
escalar=int(input("\nEscalar a multiplicar: "))


mat1=numpy.zeros((r1,c1))
matr=numpy.zeros((r1,c1))

print("Introduce la matriz: \n")
for r in range(0,r1):
    for c in range(0,c1):
        mat1[r,c]=input("Captura de matriz: ["+str(r+1)+str(c+1)+"]")

#Operacion 
for r in range(0,r1):
    for c in range(0,c1):
          matr[r,c]=mat1[r,c]*escalar

print(matr)
