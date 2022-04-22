import random



#generate random number from 1-10
n = random.randint(1,10)
chances_count = 0
max_chance_count = 4
while True:
    try:
        user_number = int(input('Guess a number between 1 to 10: '))
    except:
        print("Please Only Enter Numbers")
        break
    if user_number == n:
        print(f"Congratulations !!! Guessed Number {n} is correct")
        break
    elif user_number > n:
        print(f"Your number is greater than the random number you have only {max_chance_count-chances_count}")
    else:
        print(f"Your number is lesser than the random number you have only {max_chance_count-chances_count}")
    chances_count += 1

    print(chances_count)
    if chances_count == 4:
        print("GAME OVER..XXXXX")
        break
