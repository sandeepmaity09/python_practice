grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

print print_grades(grades)

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total

print grades_sum(grades)

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
print grades_average(grades)

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
    length = len(scores)
    variance = variance / length
    return variance
print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)