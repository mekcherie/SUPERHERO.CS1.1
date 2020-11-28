
class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print('{} is eating'.format(self.name))

  def drink(self):
    print('{} is drinking'.format(self.name))

class Frog(Animal):
    def jump(self):
        print('{} is jumping'.format(self.name))


# "EXAMPLE"
# class Animal:
#     def __init__(self, name, sleep_time):
#         self.name = name
#         self.sleep_time = sleep_time

#     def sleep(self):
#         print(
#             "{} sleeps for {} hours {}".format(
#                 self.name,
#                 self.sleep_time)
#     dog = Animal("Sophie", 12)
#     dog.sleep()


# class Animal:
#     def __init__(self, name, sleep_duration):
#         self.name = name
#         self.sleep_duration = sleep_duration

#     def sleep(self):
#         print(
#             "{} sleeps for {} hours".format(
#                 self.name,
#                 self.sleep_duration))

# # Note that the class Dog takes in Animal as a parameter!
# class Dog(Animal):
#     def bark(self):
#         print("Woof! Woof!")