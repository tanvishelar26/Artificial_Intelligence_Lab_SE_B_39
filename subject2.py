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
    @Rule(StudentFacts(likes='Electronics'), StudentFacts(likes='Maths'), StudentFacts(likes='Programming'))
    def mechatronics(self):
        print("Suggested Career Path: Mechatronics Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Artificial Intelligence'))
    def aids(self):
        print("Suggested Career Path: Artificial Intelligence and Data Science")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Artificial Intelligence'), StudentFacts(likes='Maths'))
    def roai(self):
        print("Suggested Career Path: Robotics and Artificial Intelligence")
def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("Enter any 2 Subjects from the list given:\nMaths\nPhysics\nGraphics\nArtificial Intelligence\nProgramming\n")
    
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()



