import random
def genW(randomString, size):
    word = []
    index = 0
    for index in range(size)):
      word.append(random.choice(randomString))
    return ("".join(word))
