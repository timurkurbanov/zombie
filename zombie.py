import random

class Zombie:

    max_speed = 5
  #There should be a max_strength class variable set to 8. 
    max_strength = 8
    horde = []
    plague_level = 10
    default_speed = 1
  #There should be a defaul_strength class variable set to 3. 
    default_strength = 3
#__init__() should initialize the zombie's strength as well as speed. Strength argument, value passed in is greater than the maximum strength, the default strength should be used instead.
def __init__(self, speed, strength):
    if speed > Zombie.max_speed:
        self.speed = Zombie.default_speed
    else:
        self.speed = speed
    if strength > Zombie.max_strength:
        self.strength = Zombie.default_strength
    else:
        self.strength = strength


#Implement a __str__() instance method. Try making an instance of Zombie
#Currently zombies have just one attribute: speed. add strength as a second attribute.
def __str__(self):
    return f'Speed: {self.speed}, Strength: {self.strength}'

@classmethod
def spawn(cls):
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
        speed = random.randint(1, Zombie.max_speed)
        Zombie.horde.append(Zombie(speed))
        count += 1

@classmethod
def new_day(cls):

    Zombie.spawn()
    Zombie.some_die_off()
    Zombie.increase_plague_level()

@classmethod
def some_die_off(cls):
    how_many_die = random.randint(0, 10)
    counter = 0
    while counter < how_many_die and len(Zombie.horde) > 0:
        speed = random.randint(1, Zombie.max_speed)
        random_zombie = random.randint(0,len(Zombie.horde) - 1)
        Zombie.horde.pop(random_zombie)
        counter += 1

def encounter(self):
#you should only try to fight the zombie if you don't outrun it.
#If you don't manage to outrun the zombie, call our new fight() method to try to fight it off.
#If you lose the fight, you still die.
#If you win the fight, you survive, BUT in the process you catch the zombie plague. Instantiate a new zombie object (that's you!) and add it to Zombie.horde.
#Make sure encounter always returns a string summarizing what happens (e.g. "You are now a zombie. Raawwwrghh").
# 
    outrun = self.chase()
    fight = self.fight()
    if outrun:
        return 'You escaped!'
    elif outrun:
        if fight:
            Zombie.horde.append(self)
            return 'You are now a zombie. Raawwwrghh'
    else:
        return 'You died.'

def chase(self):
  
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed

def fight(self):
#Zombie.max_strength generate a random number how you fight off zombie. return True if your streng greater than the zombie's and False otherwise.
    your_strength = random.randint(1, Zombie.max_strength)
    return your_strength > self.strength
  
# new class method increase_plague_level:
@classmethod
def increase_plague_level(cls):
#random number between 0 and 2 and increase Zombie.plague_level
    increase_number = random.randit(0, 2)
    Zombie.plague_level += increase_number

print(Zombie.horde) # []
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594f0b70>, <__main__.Zombie object at 0x7f6f594f0d68>]
zombie1 = Zombie.horde[0]
print(zombie1) # Speed: 1 -- Strength: 7
zombie2 = Zombie.horde[1]
print(zombie2) # Speed: 2 -- Strength: 7
print(zombie1.encounter()) # You escaped!
print(zombie2.encounter()) # You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594efef0>, <__main__.Zombie object at 0x7f6f594f0c50>, <__main__.Zombie object at 0x7f6f594f0cc0>]
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.encounter()) # You died!
print(zombie2.encounter()) # You escaped!
