import math

def calc_dog_age(dog_age_in_human_yrs):
   return math.log(dog_age_in_human_yrs) * 16 + 31

print(f"{calc_dog_age(1):.0f}")
print(f"{calc_dog_age(5):.0f}")
print(f"{calc_dog_age(9):.0f}")
print(f"{calc_dog_age(12):.0f}")
print(f"{calc_dog_age(55):.0f}")