import numpy

r1=int(input("Numero de filas de M1: "))
c1=int(input("Numero de columnas de M1: "))
r2=int(input("\nNumero de filas de M2: "))
c2=int(input("Numero de columnas de M2: "))


mat1=numpy.zeros((r1,c1))
mat2=numpy.zeros((r2,c2))
mat3=numpy.zeros((r1,c2))

print("Introduce la primera matriz: \n")
for r in range(0,r1):
    for c in range(0,c1):
        mat1[r,c]=input("Captura M1: ["+str(r+1)+str(c+1)+"]")

print("Introduce la segunda matriz: \n")
for r in range(0,r2):
    for c in range(0,c2):
        mat2[r,c]=input("Captura M2: ["+str(r+1)+str(c+1)+"]")

#Operacion suma
for r in range(0,r1):
    for c in range(0,c2):
          mat3[r,c]+=mat1[r,c]+mat2[r,c]

print(mat3)
