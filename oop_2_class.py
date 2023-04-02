# class
class Person:
    # class attributes
    address = 'no information'

    # constructor (yapıcı metod)
    def __init__(self, name, year):
        pass # eğer burada pass olmazsa hata alırız çünkü dolu olmalı
        
        # object attributes
        self.name = name
        self.year = year
        print('__init__ metodu çalıştı.')

    # instance methods
    def intro(self):
        print('Hello There! I am'+ self.name)  # hello there. i am serhat

    def calculateAge(self)
        2023 - self.year


    # object (instance)
    p1 = person(name = 'sude', year = 1992, address: 'istanbul')
    p2 = person(name = 'ceyda', year = 2003)

    # updating şimdi no information dğil kocaeli olarak görünür yani en son değiştirilen esas alnır
    p1.name = 'serhat'
    p2.address = 'kocaeli'

    # accessing object attributes
    print(f'p1 name:' {p1.name}, 'p1 year:' {p1.year}, 'address:' {p1.address}) 
    print(f'p2 name:' {p2.name}, 'p2 year:' {p2.year}, 'address:' {p2.address}) 

    print(p1)
    print(p2)
    print(type(p1))
    print(type(p2))    # türleri class çıkacak
    print(p1 == p2)   # false cevabını alırım

p1.intro()
p2.intro()
print(f'yaşım:' {p1.calculateAge()})
print(f'yaşım:' {p2.calculateAge()})

# yeni bir örnek

class Circle:
    # class object attribute
    pi = 3,14      # tüm değerler için geçerli olan buraya yazılır.

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # methods
    def cevre_hesapla(self):
        return 2* self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi* yaricap**2

c1 = Circle()   # burada belirtmediğimiz için yarıçapı 1 alır
c2 = Circle(5)   #yarıçapı 5 alır

print(f'c1 alan=' {c1.alan_hesapla()}, 'c1 çevresi:'{c1.cevre_hesapla()})
print(f'c2 alan=' {c2.alan_hesapla()}, 'c2 çevresi:'{c2.cevre_hesapla()})
    
   