#  a = 7 #ctr i slesh daje koemntarz do wszytskiego
# b = 5
# if a > b:
#     print('liczba a jest wieksza od liczby b')
# elif a < b :
#     print('liczba a jest mniejsza od liczby b')
# else:
#     print('liczby są równe')
#
# a = input("podaj liczbe a:")
# b = input("podaj liczbe b:")
# c = input("podaj liczbe c:")
# d = input("podaj liczbe d:")
# print(a)
# print(b)
# print(c)
# print(d)
# print(type(a))
# a = int(a)#przerabiamy typ zmiennej, moze byc tez float itd.#print(a) print(type(a))
# b= int(b)
# c = int(c)
# d = int(d)
# if(a>b) & (c>d):
#     print('liczba a jest większa od liczby b i liczba c jest większa od liczby d')
# else:
#     print('liczba a nie jest większa od liczby b i liczba c nie jest większa od liczby d')


# for i in range(0,6,1):
#     print(i)

# lista = ['napis', 3 , 4, 5.6]
# for element in lista:
#     print(element)
# else:
#     print('wyswietlenie elementów z listy zostało zakończone')

# while warunek:
#     instrukcja lub blok instrukcji
# else:
#     instrukcja lub bl.instr po zakończeniu działania pętli

# licznik = 0
# while licznik!= 10:
#     print(licznik)
#     licznik += 1
# else:
#     print('zostało wyświetlonych ' + str(licznik ) + ' liczb')

# lista=[4,6,2,3,5,9,1]
# liczba =input("wczytaj liczbę: ")
# licznik = 0
# while licznik != len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print(liczba + "-" + str(lista[licznik]) + '= 0')
#         break
#     else:
#         licznik += 1
# else:
#     print("żadna z liczb, które są na liście nie dała odpowiedniego wyniku")
#


# lista=[4,6,2,3,5,9,1]
# lista2=[7,5,3,4]
# suma =[]
# for a in lista:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#         print(suma)


# try
#     operacja np int wczytanej wartości
#     instrukcje
# except nazwa błędu:
#     instrukcje po tym jak napotkamy błąd
# else:
#     blok instrukcji bez błędu

# liczba1 = input("podaj liczbę:")
# liczba2 = input("podaj liczbę:" )
# try:
#     wynik = int(liczba1)/ int(liczba2)
#     print("wynik = " + str(wynik))
# except ZeroDivisionError:
#     print("Nie dzielimy przez 0!")
# except ValueError:
#     print("Nie wczytano liczby całkowitej")

# lista = ['coś', 4,2,6,4,5,[1, 2,3,4,5]]
# print(lista)
# print(lista[5]) #podaje element z listy
# lista.append(9)
# print(lista)
# lista.insert(1, 'element') # podajemy nr indeksu na krórym ma byc nadany i nasyęonie wartość
# print(lista)
# lista.pop(5) # usuwamy element
# print(lista)
# lista.remove('element')
# print(lista)
# lista.extend((1,2,3))
# print(lista)


# # 1 jest naszym kluczem i prrzyjmuje jakąs wartośc
# slownik = {1:22, 'klucz': 'wartosc', 3.4 :5, 1 : 16 }
# print(slownik)
# slownik[4] = 45
# print(slownik)
# slownik.pop(4)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
#
# del slownik
# print(slownik)


# for x in range(0,21,4):
#  print(x

# for x in range(10, 0, -3):
#  print(x)

# for y in range(1,11,2):
#  for x in range(1,11):
#     print('y={}, x={}'.format(y,x))

# for x in range(1,101):
#  if(x%17.5==0):
#      print("szukana liczba to {}".format(x))

# break- przerwanie instrukcji

# continue - przeskok do następnego obrotu pętli
# for x in range(-10,11):
#  if(x==0):
#     continue
# print(1/x)


# napis="ministerstwo do spraw niezbyt istotnych spraw"
# print(napis.upper())

# napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
# print(napis.lower())

# napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
# print(napis.title())  # powiększa 1 litery każdego słowa

# napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
# print(napis.replace("I","X"))  - zmiana liter i na x w słowie/ zdaniu
#  x=len("MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW")
# print(x) - liczy ilośc znaków

# napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
# print(napis.count('IS')) - liczy ilość jakiegos słowa/znaku itp.

# napis=" MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW "
# print(napis.strip()) -  usuwa spacje przed zdaniem i na koncu

# napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
# print(napis.strip("MINI")) usunie słwoo mini

# napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
# print(napis.split()) - dzieli na poszczegolne słowa

# napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
# print(napis.strip("MINI").title().replace('i','X')) - łączenie różnych funkcji

# nazwa="Llanf"
# for n in nazwa:
#  print(n) - zostanie każda litera wyswietlona'

# kriszna= "rama "*5+" "+5*"hare "
# print(kriszna) - 5 razy zostanie wyświetlona rama i 5 razy hare

# if ("X" in "Space"):
#  print("ten ciąg zawiera X!")
# else:
#  print( "nie ma ")


# lancuch="123456789"
# print(lancuch[2]) - wyciecie 2 znaku ale loczymu od 0 czyli będzie to 3!
# print(lancuch[-2]) - pobranie 2 znaku od kńca
# print(lancuch[2:5])
# print(lancuch[0:6:2]) - co drugi od 1- 7
# print(lancuch[::2]) - co drugi znak wycięty

# print(lista4[2:]) - pobranie el. z listy od 2
# print(lista4[:3]) - do poz.3 tylko
# print(lista4[:]) - wyswietlanie całej zawartości

# poszukiwani=["Michael Scofield","Lincoln Burrows","Theodore Bagwell","Uczciwy polityk"]
# if("Andrzej Klusiewicz" in poszukiwani):
#  print("pszypau")
# else:
#  print("nie pszypau")  #### lista  warunki
#
# lista=[1,2,3,4,5,6,7]
# lista.append(8)  - dodaje ele.
# print(lista)
# lista.insert(0,"X") - dodaje przed 1 X - czyli insert oznacza ze w skazanym miejscu będzie nowy elem.
# print(lista)
# lista[1]="Y" zamienia 1 na Y
# print(lista)

# lista=[1,0,2,0,3,0,4,0,5,0,6,0,7,0,3]
# del lista[2]  usuwa  ele.zawierający 2
# print(lista)
# lista.remove(3) usunie 3 ale tylko pierwszą
# print(lista)
# del lista[0:4]
# print(lista)
# lista.clear()
# print(lista) - usuwa całą listę

#  pdk=["Ogórek","Pomidor","Ziemniak","Marchew","Steven Hawking"]
# pdk.sort()
# print(pdk) - alfabetycznie sortuje
# pdk=["Ogórek","Pomidor","Ziemniak","Marchew"]
# pdk.sort()
# pdk.reverse() - alfabet.ale od końca
# print(pdk)

# from operator import itemgetter
# furki=[[3,"Renault"],[2,"Citroen"],[1,"Audi"],[4,"Zaporożec"]]
# furki.sort(key=itemgetter(1)) - sortuje alf. po markach
# print(furki)

#



# liczby=[]
# for x in range(1,21): liczby.append(x)
# print(liczby)
# parzyste=[i*10 for i in liczby] - liczby pomnożone z listy o 10 .
# print(parzyste)

# liczby=[]
# for x in range(1,21): liczby.append(x)
# print(liczby)
# parzyste=[i*10 for i in liczby if i%2==0]
# print(parzyste)

# liczby=[i for i in range(1,11)]
# parzyste=list(map(lambda x:x*2,liczby))
# print(parzyste)  - map powoduje ze trafią liczby pomnożone przez 2

# krotka=("Tytanowy Janusz","Molibdenowy Mateusz",777,"Przypadkowy
# tekst",[12,55,"koza"])
# krotka2=tuple()  -  krotki

# madness=("Longer","jeśli","to","czytasz i nie
# jesteś","lamus","to","podrzuć","jakiegoś","dobrego","mema")
# print(madness[2:7])
# print(madness[0:5:2])
# if "Longer" in madness:
#  print("Wygrałem! :D")
# for m in madness:
#  print(m)

# def sayHello(imie):
#  imie="Czesław"
#  print("Hello my friend {}!".format(imie))

# def powieksz(x):
#  return x.upper()
# def zastosuj_dla_wszystkich(fun,*args):
#  for a in args:
#      print(fun(a))
# zastosuj_dla_wszystkich(powieksz,'siała','baba','mak')

# def daj_funkcje(x):
#  def podwoj(a):
#      return a*2
#  def polowa(a):
#     return a/2
#  if x==1:
#     return podwoj
#  elif x==2:
#     return polowa
# fun=daj_funkcje(1)
# print ( fun(6))

# def args(*args):
#  for a in args:
#     print(f'{a}')
#     args(1, 2, 3, 4, 5)

# argi(*[1,2,3,4],'coś') - każdy elem. z listy zostanie wypakowany oddzielnie
# argi([1,2,3,4],'coś') - lista zostanie wypakowana i cos.

# Wyrażenia z dwoma gwiazdkami (**) stosujemy gdy do funkcji chcemy przekazać zestaw
# argumentów klucz wartość.
# def parametr_kwargs( **kwargs):
#  for k in kwargs:
#     print(k,kwargs[k])
# parametr_kwargs(dodatkowy=48, nastepny=111)

# Jeśli zechcielibyśmy do funkcji przekazać jakieś dodatkowe poza **kwargs parametry to musimy
# wymienić je jako pierwsze:
# def kwargs_argument(argument,**kwargs):
#  print(argument)
#  print(kwargs)
# kwargs_argument(argument=10,param1='Andrzej',param2='Klusiewicz')

#piosenka.py
def spiew():
    print("lalala")
def zespol():
    print("nanana")


