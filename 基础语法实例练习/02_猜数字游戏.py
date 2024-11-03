import random
number = random.randint(1,100)
guess = None

while guess != number:
    guess = int(input("猜一个1到100之间的数字："))

    if guess < number:
        print("太小了！")
    elif guess > number:
        print("太大了！")
    else:
        print ("恭喜，你猜对了！")
