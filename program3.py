try:
    a=int(input())

except ValueError :
    raise ValueError("ValueError occured ")
except KeyboardInterrupt :
    raise KeyboardInterrupt("Keyboard interrupt occur")
