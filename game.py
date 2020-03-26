# first, let us create our basic Character class

'''
# character's traits and powers/skills - each will be a list
# character will have an initial health of 10,000
# character could have an attack() function 
# idea - a regain_health() function that takes in some antidote as a parameter and 
# doesn't work with no antidote
# so 'powers_map' is a dictionary
# the keys are the power names themselves, i.e. 'flight', 'super strength', 
# 'shapeshifting', etc.
# the values are the power attack points/strength ('flight' usually has 0 atk pts, 'super strength' has 
# maybe 75 atk points)
# same for skills_map, only skills_map is for skills, i.e. 'hand-to-hand combat', 'archery', etc.

# appending a trait or power or skill to the existing list to use
# using a generic function for dictionaries since both powers_map
# and skills_map are dicts
'''
class Character:
    # class attribute, doesn't change depending on instances
    health = 10000

    def __init__(self, name, traits=[], powers_map={}, skills_map={}):
        self.name = name
        self.traits = traits 
        self.powers_map = powers_map
        self.skills_map = skills_map

    def add(self, str, num):
        n = int(input("1 - Add New Power, 2 - Add New Skill. Any Other Key? Exit")) 
        if n == 1:
            self.powers_map[str] = num
        elif n == 2:
            self.skills_map[str] = num
        else:
            exit(1) 

    def add_trait(self, trait):
        self.traits.append(trait) 

    def lose(self, n):
        # losing n health points
        self.health -= n 

    def gain(self, n):
        # gain n health points
        self.health += n

    def set_name(self, str1):
        self.name = str1

    def attack(self, Character, str):
        # Character: the character our character is attacking
        # str: the power/skill our character will use
        atk = 0 # str's value in whatever dict it came from
        test = (str in self.powers_map.keys()) # checks if the power/skill is in the powers dictionary
        test2 = (str in self.skills_map.keys()) # checks if the power/skill is in the skills dictionary

        if (test == False and test2 == False): # what if provided attack isn't in either dict?
            print(f"ERROR - attack not in {self.name}'s powers or skillset.") 
        elif test: # attack is in powers dictionary
            atk = self.powers_map[str]
            print(f"{self.name} uses {str}! {Character.name} loses {atk} health points.")
            Character.lose(atk) 
        elif test2: # attack is in skills directory
            atk = self.skills_map[str] 
            print(f"{self.name} uses {str}! {Character.name} loses {atk} health points.")
            Character.lose(atk) 


# testing ground