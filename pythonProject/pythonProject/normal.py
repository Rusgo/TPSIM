import math
import random


def normal(media, de):
    rnd1 = random.random()
    rnd2 = random.random()
    n1 = (pow(-2 * math.log(rnd1), 1 / 2) * math.cos(2 * math.pi * rnd2)) * de + media
    n2 = (pow(-2 * math.log(rnd1), 1 / 2) * math.sin(2 * math.pi * rnd2)) * de + media
    return n1, n2