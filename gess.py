import random

a = random.randint(0, 100) #random number
stop = False
while not stop :

   # print(int(a)) #check the number
    number = int(input('pleas enter a num ,0 to stop' )) #Enter a number from the user

    #print('Your choice is: ', number)


    def random():
        #print(int(a))
        return a


    x = random()

    if number == x:
        print("good!,You guessed it")
    elif number > x:
        b = int((number - x))
        print("The number of points you are missing: ", b)
    else:
        b = int((x - number))
        print("The number of unnecessary points :", b)
        stop = (number == 0)
print("buy buy")
