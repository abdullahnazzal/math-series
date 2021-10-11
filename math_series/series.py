def fibonacci(n:int)  :
    """
    Fibonacci Funtion is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    and return nth Integer
    """
    x=0
    y=1
    # count=0
    if n <=0:
        print("You Must Enter Positve Number")
    elif n==1:
        print(x)
    else:
        for i in range(n):
            print(x)
            nth=x+y
            x = y
            y = nth
        return(nth-1)
