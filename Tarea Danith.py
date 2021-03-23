#Ejercicio 1 (0-9)
for h in range(0, 10):
    print(h)

#Ejercicio 2 (100-199)
for z in range(100, 200):
    print(z)

#Ejercicio 3 De 5 en 5, saltando de 3 números
for b in range(5, 21, 3):
    print(b)

#Ejercicio 4 Números correlativos
r = int(input("Digite un número: "))
for r in range(r, r*2):
    print(r)

#Ejercicio 5-6 Listado (Vocales sin repetir)
frase = input("Frase: ")
print("Vocales en la frase:")
for c in "aeiou":
  if c in frase:
    print(c)

#Ejercicio 7 Sumatoria
total = 0
for p in range(101):
    total = total + p
print("Sumatoria:", total)

#Ejercicio 8 Rango
añoInicio=int(input("Año inicial:"))
añoFin=int(input("Año final:"))
for año in range(añoInicio, añoFin+1):
   if not año%10==0:
       continue
   if not año%4==0:
       continue
   if año%100!=0 or año%400==0:
       print(año)

# Ejercicio 9 Factorial
numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f)

#Ejecicio 10 Fibonacci
f1=0
f2=1
print(f1)
print(f2)
for i in range(8):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3