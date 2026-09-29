import random
houses = {}
cls_houses = ["Gryff", "Huff", "Raw", "Slyn"]
class Hat:

    _houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
       
        print(name, "is in", random.choice(cls_houses))

hat = Hat()
hat.sort("Harry")
