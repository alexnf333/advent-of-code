import time
import math

# main() calculates total fuel and returns processing time
# in order to be used by avg_time
def main():
    fuel_for_spacecraft = 0
    fuel_for_all_fuel = 0
    initial_time = time.time()

    with open("data.txt", "r") as spacecraft:
        for module in spacecraft:
            module_fuel = math.floor(int(module) / 3) - 2
            fuel_for_spacecraft += module_fuel
            fuel_for_fuel = module_fuel
            while True:
                fuel_for_fuel = math.floor(fuel_for_fuel / 3) - 2
                if fuel_for_fuel <= 0:
                    break
                fuel_for_all_fuel += fuel_for_fuel

    print("fuel for spacecraft: ", fuel_for_spacecraft)
    print("fuel for fuel: ", fuel_for_all_fuel)
    print("total fuel: ", fuel_for_spacecraft + fuel_for_all_fuel)

    elapsed_time = time.time() - initial_time
    print('time: {} secs'.format(elapsed_time))
    return elapsed_time

# avg_time calculates average proccesing time for the indicated number of tests
def avg_time(number_of_tests):
    return print("average time:",
                sum([main() for _ in range(number_of_tests)]) / number_of_tests)

if __name__ == '__main__':
    main()
