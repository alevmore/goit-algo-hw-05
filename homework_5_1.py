def caching_fibonacci(): ## Отримуємо функцію fibonacci
    cache = dict()
    def fibonacci (n):  
        if n <= 0:    #проводимо рекурсію
            return 0
        if n == 1: 
            return 1
        if n in cache: 
            return cache[n]
        cache [n] = fibonacci(n - 1) + fibonacci(n - 2)  # розраховуємо число Фібоначчі
        return cache [n]
    
    return fibonacci  #повертаємо внутрішню функцію

# Отримуємо функцію fibonacci через замикання
fib = caching_fibonacci()  

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
   

