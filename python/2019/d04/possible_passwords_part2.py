import time
import re

# main() calculates number of possible passwords considering
# larger group criteria
def main():
    meet = 0
    doubles = False
    ascending_sequence = True
    larger_group = None
    initial_time = time.time()

    try:
        with open("data.txt", "r") as input:
            given_range_str = input.read()

        given_range_list = re.split("-", given_range_str)
        for password in range(int(given_range_list[0]), int(given_range_list[1])+1):
            password_string = str(password)
            if len(password_string) != 6:
                continue
            for digit in range(len(password_string)-1):
                if password_string[digit] == password_string[digit+1]:
                    if doubles == False:
                        if larger_group is not False:
                            doubles = True
                            larger_group = False
                    else:
                        larger_group = True
                else:
                    doubles = False
                    if password_string[digit] > password_string[digit+1]:
                        ascending_sequence = False
                        continue
            if not larger_group and ascending_sequence:
                meet += 1
            doubles = False
            ascending_sequence = True
            larger_group = True
    except FileNotFoundError:
        print("File not found")
    except:
        print("Error found")
    print("met-criteria passwords: ", meet)
    elapsed_time = time.time() - initial_time
    print('time: {} secs'.format(elapsed_time))
    return elapsed_time

# avg_time calculates average proccesing time for the indicated number of tests
def avg_time(number_of_tests):
    return print("average time:",
                sum([main() for _ in range(number_of_tests)]) / number_of_tests)

if __name__ == '__main__':
    main()
