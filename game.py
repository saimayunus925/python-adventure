# first, let us create our basic Character class

'''
# character's traits and powers/skills - each will be a list
# character will have an initial health of 10,000
# character could have an attack() function 
# idea - a regain_health() function that takes in some antidote as a parameter and 
# doesn't work with no antidote
'''
class Character:
    # class attribute, doesn't change depending on instances
    health = 10000
    def __init__(self, traits=[], powers_map={}, skills_map={}):
        self.traits = traits 
        self.powers_map = powers_map
        self.skills_map = skills_map

    # so 'powers_map' is a dictionary
    # the keys are the power names themselves, i.e. 'flight', 'super strength', 
    # 'shapeshifting', etc.
    # the values are the power attack points/strength ('flight' usually has 0 atk pts, 'super strength' has 
    # maybe 75 atk points)
    # same for skills_map, only skills_map is for skills, i.e. 'hand-to-hand combat', 'archery', etc.
    
    # appending a trait or power or skill to the existing list to use
    # using a generic function for dictionaries since both powers_map
    # and skills_map are dicts
    def add(self, str, num):
        n = int(input("1 - Add New Power, 2 - Add New Skill. Any Other Key? Exit")) 
        if n == 1:
            self.powers_map[str] = num
        elif n == 2:
            self.skills_map[str] = num
        else:
            exit(1) 


