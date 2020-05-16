from chp9.DogClass import Dog
from chp9.subDog import SubDog

myDog = Dog('willie', 6)

print("my Dog's name is " + myDog.name.title())

myDog.sit()
myDog.roll_over()

mySubDog = SubDog("hadar")
mySubDog.sit();