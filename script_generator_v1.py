import random, string
def generator():
    letter1=random.choice(string.ascii_lowercase)
    letter2=random.choice(string.ascii_lowercase)
    letter3=random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3
    return (name)
print (generator())