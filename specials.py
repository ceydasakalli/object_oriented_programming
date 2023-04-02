myList = [1, 2, 3]
myString = 'my string'

print(len(myList))
print(len(myString))    # kaç karakter olduğunu belirtir.
print(type(myList))
print(type(myString))  
print(type(m))    # hepsi class türünde output alır fakat m tanımlı değil hata alırız.


class Movie():
    def __init__(self, title, director, duration=120):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return(f'{self.title} by {self.director}')

    def __len__(self):
        return self.duration

    def __del__(self):
        print('m metodu silindi.')

m = Movie('film adı', 'yönetmen adı', 'filmin süresi') # error alırız çünkü len ifadesine movie tanımlı değil


print(len(m))
print(str(myList))
print(str(myString))
print(len(myList))
print(len(myString))


del m 
