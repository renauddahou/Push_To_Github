import random
heads = 0
tails = 0
def coin_flip(trials):
    global heads
    global tails
    for i in range(trials):
        flip = random.randint(1,2)
        if flip == 1:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))
coin_flip(100)