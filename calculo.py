# CASO TENHA A EQUAÇÃO 

def funcao(a,b,c):
    delta = b**2 - 4*a*c

    xv = -b/2*a
    yv = -delta /4*a

    if delta > 0:
        raiz1 = (-b + delta**0.5)/ (2*a)
        raiz2 = (-b - delta**0.5)/ (2*a)
        return xv, yv, raiz1, raiz2   
    elif delta == 0:
        raiz1 = (-b + delta)/ (2*a)
        return xv, yv, raiz1, None
    else:
        return xv, yv, None, None

a= float(input("Digite o A da função: "))
b= float(input("Digite o B da função: "))
c= float(input("Digite o C da função: "))

xv,yv,raiz1,raiz2 = funcao(a,b,c)
xv = round(xv,2)
yv = round(yv,2)
print(f"O vértice esta em {xv} & {yv}")

if raiz1 != None and raiz2 != None:
    print(f"Raizes: {raiz1}, {raiz2}")
elif raiz1 != None and raiz2 == None:
    print(f"Raiz unica: {raiz1}")
else:
    print("Não possui raizes reais")

# CASO NÃO TENHA A EQUAÇÃO 

i = -10
x= []
y= []

# I = X do grafico 
while i < 10:
    x.append(i)
    f = a*i**2 + b*i +c
    y.append(f)
    i += 0.01
print(min(x))
print(min(y))
