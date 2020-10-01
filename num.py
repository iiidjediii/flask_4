def searchFib(n): # функция поиска числа Фибоначчи
    fib1=fib2=1
    while 2*n>fib1+fib2:fib1,fib2=fib2,fib1+fib2
    return fib1