class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age , track, score):
        self.name= str(name)
        self.age= int(age)
        self.tracks= track
        self.score= float(score)

        def change_name(self, change_name):
            self.change_name= change_name
            print("Student's Name", change_name)

        def change_age(self, change_age):
            self.change_age= change_age
            print("Student's Age", change_age)

        def add_track(self, add_track):
            self.add_track= add_track
            print("Student's Track", add_track)

        def get_score(self, get_score):
            self.get_score= get_score
            print("Student's score", get_score)

Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name('Peter')
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
