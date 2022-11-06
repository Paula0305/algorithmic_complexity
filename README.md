# algorithmic_complexity
Analiza złożoności obliczeniowej typowych algorytmów

Za pomocą niżej napisanego kodu, porównamy metodę rekurencyjną oraz iteracyjną w liczeniu ciągu Fibonacciego. Postaram się udowodnić, iż sposób iteracyjny jest dużo szybszy oraz pozwala na sprawne policzenie 10 000 elementów i więcej. Ciąg Fibonacciego definiujemy przypisując pierwszemu elementowi 0, natomiast drugiemu wartość 1 :

![fib od 0](https://user-images.githubusercontent.com/117033508/200172950-14d3da03-477e-4636-9a18-ee71989ff7fb.jpg)

Druga definicja mówi, iż zaczynamy przypisując zarówno pierwszemu jak i drugiemu elementowi wartość 1: 
![fib od 1](https://user-images.githubusercontent.com/117033508/200173022-8a922da0-f325-4475-9eb8-c1c12f5b7366.jpg)

I to właśnie nią będziemy się posługiwać. 


## Rekurencyjny Fibonacci
Postać rekurencyjną przedstawiamy do wyświetlenia pojedynczego wyrazu lub niewielkiej ilości, ponieważ algorytm jest bardzo niewydajny. Przy 40 elementach już wymaga, aby dłużej czekać na wynik.

```py
def fibonacci(n):
    if n < 0:
        return "Please enter a positive number"
    if(n == 0 or n == 1):
        return 1
    if n > 0:
        return fibonacci(n - 1) + fibonacci(n -2)
    else:
        return "Oops something went wrong, please try again"
```
![rekurencyjny](https://user-images.githubusercontent.com/117033508/200169987-21ca0c89-9aa7-4ef8-adc5-1c589d05b7e2.png)


## Iteracyjny Fibonacci
Drugie rozwiązanie zostanie przedstawione metodą iteracyjną, która jest wydajna i bez problemu wyznaczymy wszystkie wyrazy ciągu.

```py
def fib(n):
    count = 0
    n1 = 1
    n2 = 1
    fib_list =[]
    if n < 0:
        return "Podaj dodatnie liczby"
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


