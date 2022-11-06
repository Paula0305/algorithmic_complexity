# algorithmic_complexity
Analiza złożoności obliczeniowej typowych algorytmów

Za pomocą niżej napisanego kodu, porównamy metodę rekurencyjną oraz iteracyjną w liczeniu ciągu Fibonacciego. Postaram się udowodnić, iż sposób iteracyjny jest dużo szybszy oraz pozwala na sprawne policzenie 10 000 elementów. 

## Rekurencyjny Fibonacci

```py
def fibonacci(n):
    if n < 0:
        return "Podaj dodatnie liczby"
    if(n == 0 or n == 1):
        return 1
    if n > 0:
        return fibonacci(n - 1) + fibonacci(n -2)
    else:
        return "Coś poszło nie tak"
```
![rekurencyjny](https://user-images.githubusercontent.com/117033508/200169987-21ca0c89-9aa7-4ef8-adc5-1c589d05b7e2.png)


## Iteracyjny Fibonacci
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

## Porównanie wersji rekurencyjne i iteracyjnej
![Fibonacci_fast_vs_bad](https://user-images.githubusercontent.com/117033508/200170024-058c2f39-a9f9-4ddf-9619-0fb17b3e2608.png)


