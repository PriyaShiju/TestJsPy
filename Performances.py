import random

word="Welcome!"
for i in word:
    print(i)

"""   """
for i in range(5):
    print(random.randint(1,500))
    
performances = {'Ventriloquism':'9:00am', 
                'Snake Charmer': '12:00pm', 
                'Amazing Acrobatics': '2:00pm', 
                'Enchanted Elephants':'5:00pm'}
for i, j in performances.items():
    print(i ,':', j, sep='') 
    
"""  """

def guessing_game():
    num = random.randint(1, 10)

    guess = int(input('Guess a number between 1 and 10\n'))
    times = 1

    while guess != num:
        guess = int(input('Guess again\n'))
        times += 1
        if times == 3:
            break

    if guess == num:
        print('You win!')
    else:
        print('You lose! The number was', num)
    

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53)) 
    
    return lotto_nums
  
def main():
    answer = input('Do you want to get lottery numbers (1) or play the game (2) or quit (Q)?')
    
    if (answer == '1') :
        numbers = lotto_numbers()
        print(numbers)
    elif (answer == '2'):
        guessing_game()
    else:
        print('Toodles!')
    
main()

"""   """   

