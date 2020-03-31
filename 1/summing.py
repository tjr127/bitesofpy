def sum_numbers(numbers=None):
    sum=0
    if numbers is None:
        numbers = range(1,101)
    for number in numbers:
        sum = sum + number
    return sum

if __name__=="__main__":
    listofnumbers=[1,2,3,4,5]
    print(listofnumbers)
    print(type(listofnumbers))
    print(sum_numbers())