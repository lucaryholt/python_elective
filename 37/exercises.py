#Exercises 1

alph0 = [chr(i) for i in range(65, 91)]

#print(alph0)

alph1 = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]

#print(alph1)

alph2 = [chr(i) for i in range(65, 91) if i not in range(70, 80, 2)]

#print(alph2)


#Exercise 2

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

colors_sizes = [(c,s) for c in colors for s in sizes]

#print(colors_sizes)

#Exercise 3
#Exercise 4
#Exercise 7
