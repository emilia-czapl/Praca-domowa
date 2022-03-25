# Zadanie 1
# a = [1-x for x in range(10)]
# b = [4**i for i in range(8)]
# c = [x for x in b if x % 2 ==0]
# print(a)
# print(b)
# print(c)

#  Zadanie 2
# import random
#
# lista = [random.randint(1,100) for i in range(10)]
# print(lista)
# lista2 = [i for i in lista if i % 2 ==0]
# print(lista2)


# Zadanie 3
# lista_zakupow = {"mleko" : "litr", "chleb" : "szt", "jabłka" : "kg", "cukierki": "kg", "sok" : "litr", "papier toaletowy": "szt", "konserwy" : "szt", "batony" : "szt"}
# print(lista_zakupow)
# lista = [  k for (k,v)  in lista_zakupow.items() if v == "szt" ]
# print(lista)


# Zadanie 4
# import math
# def trojkat(a, b, c):
#     trojkat =( a * a + b * b == c * c) or a * a + c * c == b * b or c * c + b * b == a * a
#
#     if ((a * a + b * b == c * c) or (a * a + c * c == b * b)or (c * c + b * b == a * a)):
#         return("To jest trójkąt prostokątny")
#     elif ((a * a + b * b > c * c) or (a * a + c * c > b * b) or (c * c + b * b > a * a)):
#      return("To nie jest trójkąt prostokątny")
#
# print(trojkat(3,4,5))
# print(trojkat(10,10,14))
# print(trojkat(4,5,6))

#  Zadanie 5
# import math
#
#
# def pole_trapezu(a, b, h):
#     pole_trapezu =  ((a+b)/2 * h)
# a=int(input("podaj bok a:"))
# b=int(input("podaj bok b:"))
# h=int(input("podaj wysokość h:"))
# pole_trapezu = ((a+b)/2 * h)
# print(pole_trapezu)
# #
#

#
# Zadanie 8
#
# def zakupy( **kwargs):
#     print(kwargs)
#     print("Ilosc produktow: ", len(kwargs))
#     return sum(kwargs.values())
#
# liczby = {'mleko': 4, 'chleb': 3, 'jabłka': 10, 'cukierki': 19, 'sok': 3, 'papier' : 5, 'konserwy': 3, 'batony': 5}
#
# print(zakupy(**liczby))






# Zadanie 10
# plik = open("teksty.txt", "r")
#
# if plik.readable():
#     x = plik.readlines(x)
#     print(x)

#
# for x in range (0,101):
#     if x %4 ==0:
#         print(x)


# Zadanie 9
# import math
# def ciag_aryt(a1, a, n, r):
#     ciag = a1 + (n-1) * r
# r = int(input("podaj r: "))
# n = int(input("podaj n-ty wyraz ciągu : "))
# a1 = int(input("podaj a1 : "))
# ciag = a1 + (n-1) * r
# print(ciag)


# def ciag_geom(a1,q,n):
#     geo=a1 * q**(n-1)
# q = int(input("podaj q: "))
# n = int(input("podaj n-ty wyraz ciągu : "))
# a1 = int(input("podaj a1 : "))
# geo = a1 * q ** (n - 1)
# print(geo)

# import teksty._init_ as pi

# Zadanie 6
# def fun(a, b ,c):
#     fun = a *b *c
# for b in range (0,100):
#     if b == b + (4):
#         print (b)
# print(fun(1,4,10))


#