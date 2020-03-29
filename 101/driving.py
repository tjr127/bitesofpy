MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
   if age >= MIN_DRIVING_AGE:
      print(f"{name} is allowed to drive")
   else:
      print(f"{name} is not allowed to drive")

if __name__ == "__main__":
   allowed_driving('steve', 21)
   allowed_driving('jan', 18)
   allowed_driving('alan', 17)