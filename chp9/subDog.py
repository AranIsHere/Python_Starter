from chp9.DogClass import Dog


class SubDog(Dog):

    def __init__(self, name):
        self.name = name
        print("this is from SubDog:" + self.name)

