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


def lucas(n:int): 
    """
    Lucas Funtion is the series of numbers: 2, 1, 3, 4, 7, 11, 18, 29, ...
    And return nth Integer
    
    """
    x=2
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

def sum_series(n,x=0,y=1):
    """	
    Container for fibonacci, lucas funtions
    """
    if x ==0 and y==1:
        return fibonacci(n)
    elif x==2 and y==1:
        return lucas(n)

print(sum_series(5))