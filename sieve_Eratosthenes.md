# Sito Eratostenesa
Czym jest właściwie Sito Eratostenesa tudzież na czum polega? Otóż jest to przypisywany Eratostenesowi z Cyreny algorytm wyznaczania liczb pierwszych z zadanego przedziału [2,n].

Jakie są kolejne kroki, aby odpowiednio wykonać ten algorytm? 


Początkowo posiadamy cały zbiór liczb naturalnych z podanego przedziału [2, n]. Zatem nasze liczby w tablicy zaczynają się od 2 i kończą na wartości podanej n. 
Gdy już posiadamy zbiór, z którego będziemy odczytywać liczby pierwsze, wybieramy najmniejszą liczbę, czyli 2 i wykreślamy wszystkie jej wielokrotności tj. 2,4,6 ... itd

Następnie z pozostałych liczb, ponownie wybieramy najmniejszą niewykreśloną liczbę, czyli 3 i robimy to samo co dla liczby2. Zatem wykreślamy wszystkie jej wielokrotności. 
Dalej bierzemy kolejną najmniejszą niewykreśloną i usuwamy jej wielokrotności. 

Powtarzamy dotąd, dopóki nasza najmniejsza wielokrotność jest mniejsza od pierwiastka z liczby n.

![Sieve_of_Eratosthenes_animation](https://user-images.githubusercontent.com/117033508/200886485-83644aca-5c30-4e40-b73f-f5d52c3fddf9.gif)

Przejdźmy do napisania kodu w Python, który pozwoli nam na wypisanie wszystkich liczb pierwszych w danym przedziale oraz zliczy nam ich ilość.

Najpier importujemy sqrt z biblioteki math, ponieważ będziemy używać pierwiastka z liczby n. Kolejno napisałam funkcje, która wyświetla oraz zlicza ilość liczb pierwszych. 
Następnie prosimy użytkownika o podanie liczby z zakresu od 2 do n oraz zapisujemy ją w zmiennej "x" . Musimy pamiętać, aby zmienić string na typ int. 
Zabezpieczamy kod, przed wpisaniem liczby mniejszej niż, za pomocą pętli while. 
I na końcu wywołujemy funkcję, od podanej liczby. 

```py
from math import sqrt


def sieve_Eratosthenes(x):
    primes = []
    count = 1
    primes = [True] * (x + 1)  
    for i in range(2, int(sqrt(x + 1))):
        if primes[i]:
            for j in range(i + i, x + 1, i):
                primes[j] = False

    for i in range(2, x + 1):
        if primes[i]:
            print(f"Number {count} : {i}")
            count += 1

    return print(f"The number of primes in a given range is: {count}")


x = int(input("Enter a positive number greater than 2:"))
while x <= 2:
    x = int(input("Enter positiv number:"))
    
sieve_Eratosthenes(x)
```

Algorytm działa bardzo szybko, pozwala na sprawne otrzymanie liczb pierwszych z danego zakresu. 

![giphy](https://user-images.githubusercontent.com/117033508/200890188-3f52d034-65b8-475b-adc4-6dc5883f8277.gif)
