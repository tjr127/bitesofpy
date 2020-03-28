message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
   '''lines = message.split('\n')
   print(lines)
   joinlines ='|'.join(lines)
   print(joinlines)'''
   return '|'.join(message.splitlines())


if __name__ == "__main__":
   print(split_in_columns())