import time

def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        print("Your Time Left is {:02d}:{:02d}".format(mins, secs))
        time.sleep(1)
        t -= 1
    print("Time is up!")


def start():
    t = input("Enter the number of seconds: ")
    if t.isnumeric():
        countdown(int(t))
    elif t == 'q':
        exit(0)
    else:
        print("Was not a number.")
    start()


start()
