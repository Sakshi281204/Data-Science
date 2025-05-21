class Animal():
    a="Animal"
    def say():
        print("la la la la")


class Human():
    a="Human"
    def say():
        print("i am human")
an=Animal()
hu=Human()
print(an.a)
Animal.say()
print(hu.a)
Human.say()