import time
import random

name = input("Hello, what is your name? ")

# To give the user the impression its a real person add a delay before questions
time.sleep(random.randrange(5))

print("Hello " + name)

# Asking the user questions
feeling = input("How are you today? ")
time.sleep(5)
# Creating a response based on the users inputs
if "good" in feeling:
    print("I'm feeling good too!")
elif "awesome" in feeling:
    print("I'm feeling awesome too!")
elif "okay" in feeling:
    print("I know how to make your day better")
else:
    print("Chin up sunshine")

time.sleep(random.randrange(5))

favdog = input("What is your favorite dog breed? ")
# Radnomly generating a dog breed so the user feels a personal touch
dog = ["Lapsoopso", "Spaniel", "Sausage Dog"]

time.sleep(2)

print("My favourite dog is a " + random.choice(dog))
