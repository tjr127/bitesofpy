def filter_positive_even_numbers(numbers):
   list = [x for x in numbers if x % 2 == 0 if x > 0]
   return list


if __name__ == "__main__":
   numbers = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
   print(filter_positive_even_numbers(numbers))