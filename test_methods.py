import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    # given two numbers, 2 and 5
    number1 = 2
    number2 = 5

    # when we calculate the sum
    output = methods.sum_of_numbers(number1, number2)

    # then the total should be 7
    assert output == 7

def test_sub():
    # given two numbers, 9 and 6
    number1 = 9
    number2 = 6

    # when we calculate the subtraction
    output = methods.sub_of_numbers(number1, number2)

    # then the total should be 3
    assert output == 3

def test_multiply():
    # given two numbers, 32 and 2
    number1 = 32
    number2 = 2

    # when we calculate the multiplication
    output = methods.multiply_numbers(number1, number2)

    # then the total should be 64
    assert output == 64

def test_divide():
    # given two numbers, 125 and 5
    number1 = 125
    number2 = 5

    # when we calculate the division of the first number by the second number
    output = methods.divide_numbers(number1, number2)

    # then the total should be 25
    assert output == 25

