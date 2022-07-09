class student:
    def __init__(self, first_name, last_name, grade_level, courses):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_level = grade_level
        self.courses = courses
        self.email = first_name.lower()[0] + last_name.lower() + "@chs.edu"

    def promote(self):
        self.grade_level += 1

student1 = student("Kyle", "Gilbert", 9, ["French I", "Freshman English", "Algebra I", "Biology", "Art I", "American History", "Study Hall"])

print(student1.grade_level)
student1.promote()
print(student1.grade_level)

class athlete(student):
    def __init__(self, first_name, last_name, grade_level, courses, sports):
        super().__init__(first_name, last_name, grade_level, courses)
        self.sports = sports

    def add_sport(self, new_sport):
        self.sports.append(new_sport)

athlete1 = athlete("Testy", "McTesterson", 10, ["French II", "Sophmore English", "Geometery I", "Chemistry", "Physical Education", "European History", "Study Hall"], ["basketball", "baseball"])

print(athlete1.first_name, athlete1.last_name, athlete1.sports)
athlete1.add_sport("soccer")
print(athlete1.first_name, athlete1.last_name, athlete1.sports)
