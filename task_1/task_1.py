def  caching_fibonacci():
    cache ={}

    def fibonаcci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        result = fibonаcci(n-1) + fibonаcci(n-2)
        cache[n] = result
        return result
    
    return fibonаcci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
       

 