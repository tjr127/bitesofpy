message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
   split = message.split('\n')
   print(split)
   join = '|'.join(split)
   print(join)
   return join


if __name__ == "__main__":
   split_in_columns()