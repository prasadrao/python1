#!/usr/local/bin/python3
class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return "%s:%s" % (self.name, self.breed)

if __name__ == "__main__":
    global dogs
    dogs = []
    def print_lst(arg):
        for i, j in enumerate(dogs):
            print("{0}. {1}".format(i, j))
    while True:
        dog_name = input("Name: ")
        if not dog_name:
            print("Good Bye for now!!")
            break
        breed_name = input("Breed: ")
        dogs.append(Dog(dog_name, breed_name))
        print_lst(dogs)
