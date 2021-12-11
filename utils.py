from functools import reduce


def read_numbers_from_file(file_path, sep=' '):
    with open(file_path) as file:
        numbers = []
        for line in file:
            for number in line.split(sep):
                try:
                    numbers.append(int(number))
                except:
                    pass

    return numbers


def get_min(src):
    return min(src)


def get_max(src):
    return max(src)


def get_sum(src):
    return sum(src)


def get_multiply(src):
    return reduce((lambda a, b: a * b), src)


def complex_functionality(file_path, sep=' '):
    try:
        numbers = read_numbers_from_file(file_path, sep)
        get_min(numbers)
        get_max(numbers)
        get_sum(numbers)
        get_multiply(numbers)
    except:
        print('Error occured!')


