# create a class for School object
import random


class Person:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class EIT(Person):

    def __init__(self, name, nationality):
        if nationality in ["Kenya", "Ghana",
                           "Nigeria", "Ivory Coast", "South Africa"]:
            super().__init__(name, nationality)
        else:
            raise ValueError("Error!!!! Not a valid EIT!!")

    def recite_fun_fact(self, fun_facts=[]):
        return random.choice(fun_facts)

    def __repr__(self):
        return "EIT Details: Name: {} \tNationality: {}".format(
            self.name, self.nationality)


class Fellow(Person):

    def __init__(self, name, nationality, happiness_level):
        super().__init__(name, nationality)
        self.happiness_level = happiness_level

    def eat(self, food_amount):
        self.happiness_level += food_amount
        return "Man that meal was awesome. Your new happiness level is {}".format(
            self.happiness_level)

    def teach(self, teaching_hours):
        self.happiness_level -= teaching_hours
        return "Damn! That class was boring! Your new happiness level is {}".format(
            self.happiness_level)

    def __repr__(self):
        return "Fellow Details\nName: {}\nNationality: {}\nHappiness: {}".format(
            self.name, self.nationality, self.happiness_level)


class School:
    """docstring for School"""

    def __init__(self, eits=[], fellows=[]):
        self.eits = eits
        self.fellows = fellows

    def display_fellows(self):
        for fellow in self.fellows:
            print(fellow)

    def display_eits(self):
        for eit in self.eits:
            print(eit)

    def add_fellow(self, fellow):
        self.fellows.append(fellow)
        return self.display_fellows()

    def add_eit(self, eit):
        self.eits.append(eit)
        return self.display_eits()

    def read_eits(self, filename):
        with open(filename) as read_file:
            read_file.readline()
            for line in read_file.readlines():
                valid_eit = False
                eit_data = line.strip().split(",")
                try:
                    eit_object = EIT(*eit_data)
                    self.eits.append(eit_object)
                    print("Valid EIT!!!!: {}".format(eit_object.nationality))
                except ValueError:
                    print("Invalid EIT!!")
        self.display_eits()

if __name__ == "__main__":
    mest = School()

andrew = Fellow("Andrew", "Chile", 1)
francis = Fellow("Francis", "South Sudan", 2)

#cave = EIT("Cavendish", "Honduras")
#roja = EIT("Rodgers", "Kenya")

# print(cave.name)

# mest.add_eit(roja)
# print("\n")
# mest.add_fellow(andrew)
# print("\n")
# mest.add_fellow(francis)
# print("\n")
# mest.add_eit(cave)
# print("\n")

# print(andrew.teach(5))
# print("\n")
# print(francis.eat(3))
# print("\n")

# tech_facts = ["teach is cool", "tech fun fact", "i love tech"]
# print("\n")
# roja.recite_fun_fact(tech_facts)
# print("\n")
# cave.recite_fun_fact(tech_facts)
# # print("\n")
filename = input("Enter filename: ")
mest.read_eits(filename)
