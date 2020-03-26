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
    def __init__(self, traits=[], powers_or_skills=[]):
        self.traits = traits
        self.powers_or_skills = powers_or_skills


