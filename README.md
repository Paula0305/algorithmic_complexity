# ANALIZA ZŁOŻONOŚCI
Analiza złożoności obliczeniowej typowych algorytmów. Kilka przykładów,  usprawniających działanie programu. 

## ALGORYTM FIBONACCI'EGO
Za pomocą niżej napisanego kodu, porównamy metodę rekurencyjną oraz iteracyjną w liczeniu ciągu Fibonacciego. Postaram się udowodnić, iż sposób iteracyjny jest dużo szybszy oraz pozwala na sprawne policzenie 10 000 elementów i więcej. Ciąg Fibonacciego definiujemy przypisując pierwszemu elementowi 0, natomiast drugiemu wartość 1 :

![fib od 0](https://user-images.githubusercontent.com/117033508/200172950-14d3da03-477e-4636-9a18-ee71989ff7fb.jpg)

Druga definicja mówi, iż zaczynamy przypisując zarówno pierwszemu jak i drugiemu elementowi wartość 1: 
![fib od 1](https://user-images.githubusercontent.com/117033508/200173022-8a922da0-f325-4475-9eb8-c1c12f5b7366.jpg)

I to właśnie nią będziemy się posługiwać. 


## Rekurencyjny Fibonacci
Postać rekurencyjną przedstawiamy do wyświetlenia pojedynczego wyrazu lub niewielkiej ilości, ponieważ algorytm jest bardzo niewydajny. Przy 40 elementach już wymaga, aby dłużej czekać na wynik.

```py
def recurrent_fib(n):
    if n < 0:
        return "Please enter a positive number"
    if(n == 0 or n == 1):
        return 1
    if n > 0:
        return recurrent_fib(n - 1) + recurrent_fib(n -2)
    else:
        return "Oops something went wrong, please try again"
```
![rekurencyjny](https://user-images.githubusercontent.com/117033508/200169987-21ca0c89-9aa7-4ef8-adc5-1c589d05b7e2.png)


## Iteracyjny Fibonacci
Drugie rozwiązanie zostanie przedstawione metodą iteracyjną, która jest wydajna i bez problemu wyznaczymy wszystkie wyrazy ciągu.

```py
def iterative_fib(n):
    count = 0
    n1 = 1
    n2 = 1
    fib_list =[]
    if n < 0:
        return "Please enter a positive number"
    elif(n == 0 or n ==1):
        return 1
    else:
        while count <= n:
            fib_list.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return fib_list[count-1]
        
 ```
![iteracyjny](https://user-images.githubusercontent.com/117033508/200169994-ec27e577-08d7-4e5f-be7b-6781853bad29.png)

Chciałabym także przedstawić wykres liczony metodą iteracyjną dla 10 000 elementów. Jest on bardzo ciekawy, ponieważ możemy zauważyć, iż niektóre dalsze elementy są liczone szybciej. Zdażają się iteracje, iż komputer wolniej radzi sobie z mniejszymi elementami, co przedstawia wykres. 

![Fibonacci_faster_add](https://user-images.githubusercontent.com/117033508/200173796-1ee48142-fcd5-4500-ac39-3187b3e3c4f2.png)


## Porównanie wersji rekurencyjne i iteracyjnej
Poniższy wykres przedstawia szybkość obliczenia poszczególnych elementów dwiema metodami : iteracyjną i rekurencyjną. Widzimy, iż wykres rekurencyjnej wersji (ciemnoniebieska linia przerywana) już przy 25 elemencie ciągu, zaczyna znacząco zwiększać czas, który jest potrzebny do obliczenia elementu. W tym samym czasie wersja iteracyjna ( jasnobłekitna linia ciągła) pozostaje praktycznie w nienaruszonym stanie. Dalej przy 35 elemencie jest ultra blisko wartości 0s. 


![Fibonacci_fast_vs_bad](https://user-images.githubusercontent.com/117033508/200170024-058c2f39-a9f9-4ddf-9619-0fb17b3e2608.png)


Wniosek zatem jest bardzo prosty. Zdecydowanie lepszą metodą jest liczenie iteracyjne ciągu Fibonacciego :)

![image](https://user-images.githubusercontent.com/117033508/200325867-5fe4890f-42ba-47f0-bd16-60c28e2c93ac.png)


## WYSZUKIWANIE BINARNE 

Przechodząc dalej, porównamy wyszukiwanie binarne za pomocą kodu w wersji rekurencyjnej i iteracyjnej. Które jest szybsze, jaka ilość operacji zostanie wykonana, aby znaleźć odpowiednią liczbę oraz ile czasu to zajęło. 

## Wyszukiwanie rekurencyjne

Sprawdzając czy liczba L znajuje się w 1000 elementowej liście, przy zastosowaniu standardowej pętli for, w najggorszym wypadku wykonamy 1000 iteracji. Musimy sprawdzać element, po elemencie. Wiadomo, może się zdarzyć, że nam się poszczęści i szukana liczba będzie na jednym z pierwszych miejsc. Jednak nadzieja Matką głupich jak to mówią. 

```py
def recurrent_search(x, dataset):

    for idx, number in enumerate(dataset):
        if(x == number):
            return "The number you are looking for is in place number: " + str(idx)
    return -1
```      

## Wyszukiwanie iteracyjne

Wyszukiwanie za pomocą algorytmu binarnego, jest dużo wydajniejsze i szybsze przy większych rozmiarach tablicy. W wersji rekurencyjnej dla 1000 elementów musieliśmy wykonać w najgorszym wypadku, aż 1000 iteracji, tutaj tylko 10 !!!

```py
def iterative_search(search_number, dataset):
    left = 0 
    right = len(dataset) 
    index = 0 
    
    while left < right: 
        index = (left + right) // 2
        if dataset[index]==search_number: 
            return "The number you are looking for is in place number: " + str(index) 
        else: 
            if dataset[index]<search_number: 
                left = index+1 
            else: 
                right = index 

    return -1
```
## Porównanie wersji rekurencyjnej i iteracyjnej

Sprawdźmy zatem czas wyszukiwania, dla obu wersji wykorzystując tablice o wielkościach 10 , 1000, 10 000

```py
from timeit import default_timer as timer


def calculate_recurrent_search(n,dataset):
    start = timer()
    recurrent_search(n,dataset)
    end = timer()
    return end - start

def calculate_iterative_search(n,dataset):
    start = timer()
    iterative_search(n,dataset)
    end = timer()
    return end - start
```

