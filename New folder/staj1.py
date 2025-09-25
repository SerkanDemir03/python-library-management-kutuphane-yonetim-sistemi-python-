import sys
import time

"""
sys.version > python versiyonu
sys.platform > platform bilgisi
sys.path > python path bilgisi

print(sys.version)
print("--------------------------------")
print(sys.platform)
print("--------------------------------")
print(sys.path)
"""
#print(objects, sep ="", end="", file=x, flush=flush)

#print("Hello","World")
#print("16","09","2025", sep="-")

#print("Hello", end=" ")
#print("World") 

"""
with open("log.txt", "w") as file:
    print("Bu bir log satiridir.", file=file)

with open("log2.txt", "w") as file:
    print("Bu bir log satiridir.", file=file)
"""

"""
print("Bekle...", end =" " ,flush=False)
time.sleep(3)
print("Bitti!")
"""

"""
#f-string
name = "Ozan"
print(f"Merhaba {name}")
name = "Ozan"
print("Merhaba", name)
print("https://www.google.com:443/api/v1/",name,"/views/cics/cregsys")
print(f"https://www.google.com:443/api/v1/{name}/views/cics/cregsys")
"""
"""
#degiskenler
#integer  (int)
sayi = 5
print(sayi)
print(type(sayi))

#string (str)
ad = "Ozan"
print(ad)
print(type(ad))

#float (float ploating)
sayi2 = 5.5 
print(sayi2)
print(type(sayi2))

#boolean (bool)
durum = False
print(durum)
print(type(durum))

#empty value (None)
bos = None
print(bos)
print(type(bos))


#DEĞİŞKEN ADLANDIRMA KURALLARI
#NOT Değişken isimleri sayısal ifade ve özel karakterler ile başlayamaz
# Değişken isimleri boşlıuk içeremez.
# Değişken isimleri karakter veya  _ ile başlamalıdır.a
"""
"""
True , False, None, if, for, while , import
"""
"""
TrueA= 5 
print(TrueA)
print(type(TrueA))

_sayi1 = 5
print(_sayi1)

sayi_9_sayi2 = 5
print(sayi_9_sayi2)

#Case sensitive
A = 5
a = 10
print(A)
print(a)

#Değişken adlandırma stilleri

#1 snake_case
sayi_1 = 5
print(sayi_1)

#2 camelCase
ozanBerk = "Ozan Berk"
print(ozanBerk)

#3 PascalCase 
OzanBerk = "Ozan Berk"
print(OzanBerk)

#4 UPPER_CASE 
OZAN_BERK = "Ozan Berk"
print(OZAN_BERK)
"""
"""
#Multiple Assignment (Çoklu Atama)
a, b, c = 1, 2, 3
print(a, b, c)

a , b, c = 1 , "Ozan" , 2 
print(a, b, c)

a,b,_ = 1,2,3
print(a,b,_)
"""
"""
#Immutable (Değiştirilemez)
a = b = c = 1
b = 2
print(a,b,c)

#Mutable (Değiştirilebilir)
a = b = c = [1,2,3]
b[1] = 10
print(a,b,c)
"""

"""
#11 Klavyeden Değer Alma
sayi = 10 
print("Sayimiz: " , sayi)

name = input("Adiniziz: ")
print("Adiniz: ", name)

age = input("Yasiniz:")
print("Yasiniz: ", age)
print(type(age))

print("--------------------------------")

age = int(input("Yasiniz: "))
print("Yasiniz: ", age)
print(type(age))
"""

#SPLIT KULLANIMI
sayi1 , sayi2 = input("Sayilari Giriniz:").split()
x = int(sayi1)
y = int(sayi2)
print(sayi1)
print(sayi2)
print(type(sayi1))
print(type(sayi2))
print(x)
print(y)
print(type(x))
print(type(y))






