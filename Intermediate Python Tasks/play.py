class InvalidInputError(Exception):pass
import random
tries=5
def play():
    x=random.randint(1,10)
    # print(x)
    for i in range(tries):
        y=int(input("Guess the number "))
        try:
            if y<=10 and y>=1:
                pass
            else:
                raise InvalidInputError
        except InvalidInputError as e:
            print("InvalidInputError\nEnter a number between 1 to 10")
        finally:
            print("\n")
        if x==y:
            print("Guessed correctly")
            break
        else:
            print("Incorrect guess")
    again=""
    again=input("Y to play again\n N for exiting\n")
    if again=="N":
        pass
    else:
        play()
play()
