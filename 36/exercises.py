#Exercise 2
print("ex2\n")

def sToL(x):
    vowels = ['a','e','y','u','i','o','å','æ','ø']
    li = []
    for i in x:
        if i not in vowels:
            li.append(i)
    li = sorted(li)
    return li

print(sToL("xheja"))

#Exercise 3
print("ex3\n")

l = ['Claus', 'Ib', 'Per']

print(sorted(l))

print(sorted(l, reverse = True))

print(sorted(l, key=len))

def lastLetter(x):
    return x[-1]

print(sorted(l, key=lastLetter))

def aInName(x):
    return 'a' not in x

print(sorted(l, key=aInName))

#Exercise 4
print("ex4\n")
lyrics = open("lyrics.txt", "w+")
songs = open("songs.txt", "w+")

lines = ['Heya beya', 'what up hater' ,'c ya later']

for i in lines:
    songs.write(i)
    songs.write("\n")

lyrics.close()
songs.close()

readSongs = open("songs.txt", "r")

print(readSongs.read())

readSongs = open("songs.txt", "r")
print(readSongs.readline())

readSongs = open("songs.txt", "r")
print(readSongs.readlines())

#Exercise 5

tup = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

print(sorted(tup))
