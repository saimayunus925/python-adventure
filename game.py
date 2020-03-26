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
    def __init__(self, atk, traits=[], powers_map={}, skills=[]):
        self.traits = traits 
        self.powers_map = powers_map
        self.atk = atk
        self.skills = skills

    # so 'powers_map' is a dictionary
    # the keys are the power names themselves, i.e. 'flight', 'super intelligence', 
    
    # appending a trait or power or skill to the existing list to use


