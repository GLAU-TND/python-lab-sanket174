try:
    a=int(input())

except ValueError as e:
    raise ValueError("ValueError occured ")
except KeyboardInterrupt as e:
    raise KeyboardInterrupt("Keyboard interrupt occur")
except EOFError as e:
    raise EOFError("EOFError occured")
