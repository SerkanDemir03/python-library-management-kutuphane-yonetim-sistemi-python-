#1 BLOCK INDENTATION
"""
x = 5 
if x > 0:
    print("x is positive")
else:
    print("x is negative")

def topla(a,b):
    sonuc = a + b
    return sonuc

i = 5 
for i in range(19):
    print(i)
    if i == 6:
        print("i esittir 6")
    else:
        print("i 6'ya esit degil")
"""
#2 COLLECTIONS - LIST
"""
a = [1,2,3]
#    0 1 2
print(a)
b = list([1,2,3,4,5])
print(b)
print(type(b))
c = []
print(c)
print(type(c))
c = 5
print(c)
print(type(c))  #INT
a= c
print("A:", a)
print("C:", c)
print(type(a))
print(type(c))  #LIST
print(c) 
"""
#3 INDEXING
"""
a = [1,2,3]
#    0 1 2
print(a)
d = a[0]
print(d)
print(type(d)) #INT
"""
#4 SLICING
#BİR KOLEKSİYONUN BELİRLİ BİR PARÇASINI ALMAK İÇİN KULLANDIĞIMIZ BİR YÖNTEM
#collection[start:stop:step]
"""
a = [10,20,30,40,50]
print(a[1:3])  #1. INDEXTEN BASLA 3.INDEXE KADAR AL AMA 3.INDEX HARIC
print(a[:4])   #BASTAN BASLA 4.INDEXE KADAR AL AMA 4.INDEX HARIC
print(a[2:])   #2. INDEXTEN BASLA LISTENIN SONUNA KADAR AL
print(a[::2])  #BASLANGICINDA BIRAKARAK 2'LI ARTIRARAK AL
import sys
#print(sys.version)
#text2 = sys.version
text = "Python"
print(text[0:6])
print(text[-3:]) #SON 3 KARAKTER AL
print(text[::-1])  #TERS YAZDIRIR
"""
#5 LIST METHODS
#append, extend, insert , pop, remove, clear, sort , reverse, index ,copy ,in , not in, all, any
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)

#1- Append > Listenin sonuna yeni bir eleman eklemek için kullanılan method
listA.append(6)
print("APPEND SONRASI LISTEMIZ: ", listA)

#2- Extend > Listenin sonuna birden fazla eleman eklemek için kullanılan method
listA.extend([7,8])
print("EXTEND SONRASI LISTEMIZ: ", listA)

#3 Insert > Listenin belirli bir indeksine yeni bir eleman eklemek için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)

listA.insert(1,7)
print("INSERT SONRASI LISTEMIZ: ", listA)

#4 Pop > Indexteki elemanı silmek için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
listA.pop() #SON ELEMANI SILER
listA.pop(1) #1. INDEKSTEKI ELEMANI SILER
print("POP SONRASI LISTEMIZ: ", listA)

#5 Remove > istenilen elemanı silmek için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
listA.remove(3)
print("REMOVE SONRASI LISTEMIZ: ", listA)

#6 Clear > listenin tüm elemanlarını silmek için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
listA.clear()
print("CLEAR SONRASI LISTEMIZ: ", listA)

#7 Sort > listenin elemanlarını küçükten büyüğe sıralamak için kullanılan method
listA = [1,3,6,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
listA.sort() #KUCUKTEN BUYUGE DOGRU SIRALAR
print("SORT SONRASI LISTEMIZ: ", listA)
listA.sort(reverse=True) #BUYUKTEN KUCUGE TERS SIRALAR
print("SORT SONRASI LISTEMIZ: ", listA)

#8 Reverse > listenin elemanlarını ters çevirmek için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
listA.reverse()
print("REVERSE SONRASI LISTEMIZ: ", listA)

#9 Index > istenilen elemanın indexini bulmak için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
print("INDEX:" , listA.index(3)) #3. ELEMANIN INDEXINI BULUR #2.INDEX

#10 Copy > listenin kopyasını oluşturmak için kullanılan method
listA = [1,2,3,4,5]
listB = listA.copy()
print("BASLANGIC LISTEMIZ: ", listA)
print("COPY SONRASI LISTEMIZ: ", listB)

#11 In > istenilen elemanın listenin içinde olup olmadığını kontrol etmek için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
print("IN:" , 6 in listA) #3. ELEMANIN LISTE ICI VAR MI KONTROL EDER #TRUE

#12 Not In > istenilen elemanın listenin içinde olup olmadığını kontrol etmek için kullanılan method
listA = [1,2,3,4,5]
print("BASLANGIC LISTEMIZ: ", listA)
print("NOT IN:" , 3 not in listA) #3. ELEMANIN LISTE ICI YOK MU KONTROL EDER #FALSE
print("NOT IN:" , 6 not in listA) #6. ELEMANIN LISTE ICI YOK MU KONTROL EDER #TRUE

#13 ALL > listenin tüm elemanlarının True olup olmadığını kontrol etmek için kullanılan method
listA = [1,2,3,4,5,-1,-2]
print("ALL SONRASI LISTEMIZ: ", all(listA)) #True
listA = [1,2,3,4,5,-1,-2,0]
print("ALL SONRASI LISTEMIZ: ", all(listA)) #False
listA = [1,2,3,4,5,-1,-2,0,[]]
print("ALL SONRASI LISTEMIZ: ", all(listA)) #False

#14 ANY > listenin bir veya birden fazla elemanının True olup olmadığını kontrol etmek için kullanılan method
listA = [1,2,3,4,5,-1,-2]
print("ANY SONRASI LISTEMIZ: ", any(listA))
listA = [1,2,3,4,5,-1,-2,[],[]]
print("ANY SONRASI LISTEMIZ: ", any(listA)) 
listA = [0,0,0,0,0]
print("ANY SONRASI LISTEMIZ: ", any(listA)) 
bool2 = [False,False,False]
print("ANY SONRASI LISTEMIZ: ", any(bool2))

#KÜTÜPHANE TAKİP SİSTEMİ
# kitaplar = []
# ÖZELLİKLER
# 1- KİTAP EKLEME 
# 2- KİTAP SİLME
# 3- KİTAPLARI LİSTELEME
# 4- KİTAP ARA
# 5- ALFABETIK OLARAK SIRALAMA
# 6- KİTAP SAYISI  -> #COUNT
# 7- KİTABIN INDEXINI BUL
# 8- LISTEYI KOPYALA
# 9- LISTEYI TEMIZLE
# 10- LISTE BOS MU DEGIL MI KONTROL ETME
# 11 - CIKIS

#LOG TUT.





