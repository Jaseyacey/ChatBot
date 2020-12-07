import time
import random

name = input("Hello, what is your name? ")

# To give the user the impression its a real person add a delay before questions
time.sleep(2)

print("Hello " + name)


feeling = input("How are you today? ")
time.sleep(random.randrange(5))
if "good" in feeling:
    print("I'm feeling good too!")
elif "awesome" in feeling:
    print("I'm feeling awesome too!")
else:
    print("Chin up sunshine")

time.sleep(random.randrange(5))

favdog = input("What is your favorite dog breed? ")

dog = ["Lapsoopso", "Spaniel", "Sausage Dog"]

time.sleep(2)

print("My favourite dog is a " + random.choice(dog))
