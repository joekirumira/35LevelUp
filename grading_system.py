
def grading_system():
    grades = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    list1 = []
    list2 = []
    for number in grades:
        if number > 50:
            list1.append(number)
        else:
            if number < 50:
                list2.append(number)

    for number in grades:
        if 100 >= number >= 90:
            print("Excellent")
        elif 89 >= number >= 70:
            print("Very good")
        elif 69 >= number >= 60:
            print("Good")
        elif 59 >= number >= 40:
            print("Poor")