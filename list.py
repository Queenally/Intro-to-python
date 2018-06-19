#x = int(raw_input('please enter the year you were born'))
#y = 2018
favfoods = ['fries','chocolate', 'icecream']
for food in favfoods:
    print(food)
grocerylist = ['bread','eggs','milk','chips','juice']
for grocery in grocerylist:
    print(grocery)
grocerylist.append('cookies')
print(grocerylist)
colors = ['blue', 'black','purple','gold']
print(colors.index('gold'))
colors.insert(2, 'red')
print(colors)
weather = []
w = raw_input('How is the weather today? ')
weather.append(w)
print(weather)
futurecareer = ['DJ','doctor','vet','coach']
print('your career is index: ',futurecareer.index('DJ'))
futurecareer.append('Futbol player')
print(futurecareer)
futurecareer.insert(1, 'professional sleeper')
print(futurecareer)