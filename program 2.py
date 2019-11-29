try:
    n=int(input())
    b=int(input())
    a=input()
    c=n+b
    l=a+b
    n.append(3)
    print(n)
except ValueError:
    raise ValueError("ValueError raised")
except AttributeError:
    raise AttributeError("AttributeError raised")
except TypeError:
    raise TypeError("TypeError raised")