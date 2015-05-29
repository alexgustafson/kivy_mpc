print("test")

class Person():

    def __init__(self, name):
        self.name = name
        self.birthday = ""
        self.haircolor = ""

    def say_hello(self):
        print( "Hello, my name is {0}".format(self.name) )

    def eating(self, food):
        if food == "spinach":
            print("Yuck, i hate {0}".format(food))
        else:
            print("Yum, i like {0}".format(food))

person = Person("Frank")
person.birthday = "today"
person.haircolor = "blue"
person.eating("spinach")
person.eating("cheese cake")
person.say_hello()



class Sequence():

    def __init__(self):
        self.volume = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pitches = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def note_on(self, note_number, pitch, volume):
        self.volume[note_number] = volume
        self.pitches[note_number] = pitch
        return self

    def play(self):
        pass



my_seq = Sequence()
my_seq.note_on(0, 10, 24)
my_seq.note_on(4, 10, 24)
my_seq.note_on(8, 10, 24)
my_seq.note_on(12, 10, 24)

my_seq.play()



