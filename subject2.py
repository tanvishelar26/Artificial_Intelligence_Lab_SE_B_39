from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Graphics'), StudentFacts(likes='Maths'))
    def civil(self):
        print("Suggested Career Path: Civil Engineering")
    @Rule(StudentFacts(likes='Electronics'), StudentFacts(likes='Maths'))
    def mechatronics(self):
        print("Suggested Career Path: Mechatronics Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Artificial Intelligence'))
    def aids(self):
        print("Suggested Career Path: Artificial Intelligence and Data Science")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Robotics'))
    def robotics(self):
        print("Suggested Career Path: Robotics Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotechnology(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Chemistry'), StudentFacts(likes='Physics'))
    def chemical(self):
        print("Suggested Career Path: Chemical Engineering")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Physics'))
    def biomedical(self):
        print("Suggested Career Path: Biomedical Engineering")
def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("""Enter any 2 subjects from the list given:
Maths
Physics
Graphics
Artificial Intelligence
Programming
Biology
Chemistry
Circuits
Electronics
Robotics
""")

    sub1 = input("Enter your 1st subject: ")
    sub2 = input("Enter your 2nd subject: ")

    engine.declare(StudentFacts(likes=sub1.strip()))
    engine.declare(StudentFacts(likes=sub2.strip()))
    engine.run()

if __name__ == "__main__":
    main()


