# algorithmic_complexity
Analiza złożoności obliczeniowej typowych algorytmów

##Rekurencyjny Fibonacci

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

##Iteracyjny Fibonacci

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

![pobrane](https://user-images.githubusercontent.com/117033508/200164888-4bf90a4f-83a1-4787-b2e9-a22bff937898.png)
