class Animal() :
    size = 'Large'
    colour = 'Brown'
    noise = 'Grunt'
    tail = 'Yes'
    legs = 4

class Dog(Animal) :
    name = 'Jimmy'
    size = 'Small'
    noise = 'Bark'
    
techno = Dog()
techno.name = 'Techno'
techno.colour = 'Black and Brown'
attribute =''
while attribute != 'nothing' :
    attribute = input("Hi, my name is Techno. What do you want to know about me? ").lower()
    if attribute != 'nothing' :
        if attribute == 'colour' :
            print(str(techno.colour))
        elif attribute == 'legs' :
            print(str(techno.legs))
        elif attribute == 'name' :
            print(str(techno.name))
        elif attribute == 'size' :
            print(str(techno.size))
        elif attribute == 'noise' :
            print(str(techno.noise))
        elif attribute == 'tail' :
            print(str(techno.tail))
        else :
            print("Sorry, I don't know about that. Please ask something else.")
print('Have a nice day.')