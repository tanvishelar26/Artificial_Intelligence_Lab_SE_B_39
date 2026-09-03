print("Choose the subject you like from the following: maths, physics, programming, biology, chemistry, circuits")

sub1 = input("Enter the subject you like:")
sub2 = input("Enter the 2nd subject you like:")

if sub1 == "maths" and sub2 == "physics":
    print("Suggest career path: Mechanical Engineering")

elif sub1 == "programming" and sub2 == "maths":
    print("Suggest career path: Computer Engineering")

elif sub1 == "biology" and sub2 == "chemistry":
    print("Suggest career path: Biotechnology")

elif sub1 == "circuits" and sub2 == "maths":
    print("Suggest career path: Electronic Engineering")

elif sub1 == "physics" and sub2 == "programming":
    print("Suggest career path: Robotics Engineering")

elif sub1 == "chemistry" and sub2 == "physics":
    print("Suggest career path: Chemical Engineering")

elif sub1 == "biology" and sub2 == "programming":
    print("Suggest career path: Biomedical Engineering")

else:
    print("Suggest career path: Explore subjects")
