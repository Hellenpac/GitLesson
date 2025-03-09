import random
# This is my first Python program hosted on Github
def roll_dice():
    '''This function rolls two dice'''
    print(random.randint(1, 7), random.randint(1, 7))

def roll_one_die():
    '''This function rolls one die'''
    print(random.randint(0,7))
    
def roll_three_dice():
        roll_one_die()
        roll_one_die()
        roll_one_die()

if __name__ == "__main__":
    roll_dice()
    roll_one_die()
    print()
    roll_three_dice()
