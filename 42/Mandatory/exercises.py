# Ex 1
print("\t\tEXERCISE 1\n\n")

board_of_directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}

management = {"Tine", "Trunte", "Rane"}

employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

print("who in the board of directors is not an employee?")

print(board_of_directors.difference(employees))

print("who in the board of directors is also an employee?")

print(board_of_directors.intersection(employees))

print("how many of the management is also member of the board?")

print(len(management.intersection(board_of_directors)))

print("All members of the managent also an employee")

print(management.intersection(employees))

print("All members of the management also in the board?")

print(management.intersection(board_of_directors))

print("Who is an employee, member of the management, and a member of the board?")

print(management.intersection(board_of_directors, employees))

print("Who of the employee is neither a memeber or the board or management?")

print(employees.difference(board_of_directors, management))

# Ex 2
print("\n\n\t\tEXERCISE 2\n\n")

datastructure = {"a": "Alpha", "b" : "Beta", "g": "Gamma"}

list_of_tuples = [(i, datastructure[i]) for i in datastructure]

print("list of tuples: " + str(list_of_tuples))

# Ex 3
print("\n\n\t\tEXERCISE 3\n\n")

set_0 = {"a", "e", "i", "o", "u", "y"}
set_1 = {"a", "e", "i", "o", "u", "y", "æ", "ø", "å"}

union = set_0.union(set_1)

print("union: " + str(union))

symmetric_difference = set_0.symmetric_difference(set_1)

print("symmetric_difference: " + str(symmetric_difference))

difference = set_0.difference(set_1)

print("number of items in set_0 and not in set_1: " + str(len(difference)))

disjoint = set_0.isdisjoint(set_1)

print("elements in set_0 are not present in set_1: " + str(disjoint))

# Ex 4
print("\n\n\t\tEXERCISE 4\n\n")

month_name_to_number = {
    "JAN" : 1,
    "FEB" : 2,
    "MAR" : 3,
    "APR" : 4,
    "MAY" : 5,
    "JUN" : 6,
    "JUL" : 7,
    "AUG" : 8,
    "SEP" : 9,
    "OCT" : 10,
    "NOV" : 11,
    "DEC" : 12
}

def dateFormatter(date_string):
    date_split = date_string.split("-")
    return (int(date_split[0]), month_name_to_number[date_split[1]], int(date_split[2]))

print("Date formatted: " + str(dateFormatter("8-MAR-85")))
