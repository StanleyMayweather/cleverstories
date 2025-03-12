"""
For this assignment, you will implement a program that asks the user for a series of words
 and then displays the story with the user's words inserted into the appropriate places.

The program should begin by asking the user for each of the words. It should then, fill those words 
into the appropriate places in the story.

To begin, please use the following story:

The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family.

Make sure to match the punctuation and spacing of the original story exactly (for example, you should
 not put your words on their own line, they should fit naturally into the story).

Also, make it so that the "exclamation" word is automatically capitalized, because it starts a new
sentence.
"""
print("The other day, I was really in trouble. It all started when I saw a very")
adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
print("down the hallway. ")
#print(f"{adjective} {animal} {verb} down the hallway. ")
exclamation = input("Exclamation: ")
print("I yelled. But all I could think to do was to")
verb2 = input("Verb: ")
print("over and over. Miraculously, that caused it to stop, but not before it tried to")    
verb3 = input("Verb: ")
print("right in front of my family.")
# This is the story line
#story = "The other day, I was really in trouble. It all started when I saw a very " + adjective + " " + animal + " " + verb + " down the hallway. " + exclamation.capitalize() + "! I yelled. But all I could think to do was to " + verb2 + " over and over. Miraculously, that caused it to stop, but not before it tried to " + verb3 + " right in front of my family."
print(f"The other day, I was really in trouble. It all started when I saw" 
f"a very {adjective} {animal} {verb} down the hallway. {exclamation.capitalize()}! I yelled." 
f"but all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop," 
 f"but not before it tried to {verb3} right in front of my family.")