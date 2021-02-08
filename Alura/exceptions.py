try:
    10/0 
    print("I'm back!")
except TypeError:
    print('Zero division not allowed!')
finally:
    print("Inside Finally")