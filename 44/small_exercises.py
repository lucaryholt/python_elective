import time

def timestamp(func):
    def wrapper(*args):
        result = func(*args)
        with open('log.txt', 'a') as f:
            f.write('Function "' + func.__name__ + '" was called on timestamp: ' + str(time.time()) + '. \nResult was: ' + str(result) + '\n\n')
    return wrapper

@timestamp
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

#add(1,2,6)

@timestamp
def printer(text):
    print(text)
    print(text)

printer('heyo')
