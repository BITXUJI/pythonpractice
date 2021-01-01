import random
import string


print(random .random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print(random.choices([1, 2, 3, 4], k=4))
print(random.choices("abcdefghi", k=4))
print("".join(random.choices(string.ascii_uppercase+string.digits, k=4)))
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)


numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
