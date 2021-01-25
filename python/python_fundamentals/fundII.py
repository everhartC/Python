def print_greeting(name, num=1):
    if type(num) != int:
        return "Must pass int"
    for i in range(num):
        print(f"Hello {name} welcome to python")
    return [num, name]

#print(print_greeting("Cam",num=10))


canvas = [
    [2,3,5,4,6],
    [6,7,4,7,9],
    [3,4,3,2,1],
    [8,8,6,3,1]
]

#print(canvas[0][1])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

#print(sports_directory['soccer'][1])

for sport in sports_directory:
    for i in range(len(sports_directory[sport])):
        print(sport, sports_directory[sport][i])