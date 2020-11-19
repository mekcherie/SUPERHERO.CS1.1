# dog.py
class Dog:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    def bark(self):
        print("Woof!")

# instantiation call that creates a Dog object:
# but now we've assigned it to the value of the my_dog variable

# print(my_dog)
# print(my_dog.name)
# # Adding the "breed" property on the fly
# my_dog.breed = "SuperDog"
# # will print "SuperDog"
# print(my_dog.breed)