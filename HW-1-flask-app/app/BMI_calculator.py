def bmi_calculator(weight, height):
    """
    A function to calculate the body mass index (BMI) of an individual 
    weight in pounds (lb), height in inches (in)
    """
    bmi = (weight / (height**2)) * 703

    return bmi