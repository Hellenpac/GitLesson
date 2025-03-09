import random
# This is my first Python program hosted on Github
def roll_dice():
    '''This function rolls two dice'''
    print(random.randint(1, 7), random.randint(1, 7))

def roll_one_die():
    '''This function rolls one die'''
    print(random.ranint(0,7))
    
if __name__ == "__main__":
    roll_dice()
    roll_one_die()
