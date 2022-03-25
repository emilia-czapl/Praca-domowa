import math
def ciag_aryt(a1, a, n, r):
    ciag = a1 + (n-1) * r
r = int(input("podaj r: "))
n = int(input("podaj n-ty wyraz ciągu : "))
a1 = int(input("podaj a1 : "))
ciag = a1 + (n-1) * r
print(ciag)


def ciag_geom(a1,q,n):
    geo=a1 * q**(n-1)
q = int(input("podaj q: "))
n = int(input("podaj n-ty wyraz ciągu : "))
a1 = int(input("podaj a1 : "))
geo = a1 * q ** (n - 1)
print(geo)