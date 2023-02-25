def intRoman(num):
  # the important numbers to initilize are 1,4,5,9 and those end with 0 to show the loop
  romanNums = {
    1000: 'm',
    900: 'cm',
    500: 'd',
    400: 'cd',
    100: 'c',
    90: 'xc',
    50: 'l',
    40: 'xl',
    10: 'x',
    9: 'ix',
    5: 'v',
    4: 'iv',
    1: 'i'
  }

  romanNum = ''
  for value, numeral in romanNums.items():
    while num >= value:
      romanNum += numeral
      num -= value

  return romanNum


num = int(input("Type a value to be changed to Roman value: "))
romanNum = intRoman(num)
print(f"Roman value of {num} is: {romanNum}")


def romanInt(romanNum):
  romanNums = {
    'm': 1000,
    'cm': 900,
    'd': 500,
    'cd': 400,
    'c': 100,
    'xc': 90,
    'l': 50,
    'xl': 40,
    'x': 10,
    'ix': 9,
    'v': 5,
    'iv': 4,
    'i': 1
  }
  #integers starts from 0
  #initilize i to zero for loop
  int = 0
  i = 0
  while i < len(romanNum):
    # if else sequence in while loop
    if i + 1 < len(romanNum) and romanNum[i:i + 2] in romanNums:
      int += romanNums[romanNum[i:i + 2]]
      i += 2
    else:
      int += romanNums[romanNum[i]]
      i += 1

  return int


romanNum = input("Type a Roman value to be changed to integer: ")
num = romanInt(romanNum)
print(f"Number value of {romanNum} is: {num}")
