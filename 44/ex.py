import time

def timer_deco(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print('Timer: ' + str(end - start))
    return wrapper

def slow_down(func):
    def wrapper(*args):
        time.sleep(1)
        func(*args)
    return wrapper

@slow_down
def countdown(n):
     if not n:   # 0 is false, not false is true
         return n
     else:
         print(n, end=' ')
         return countdown(n-1) # call the same function with n as one less

countdown(5)
