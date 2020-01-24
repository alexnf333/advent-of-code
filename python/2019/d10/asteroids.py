import time
from math import atan2, sqrt, pi
from operator import itemgetter

# asteroids_in_sight returns number of asteroids in sight and a list with
# asteroid information and destruction order
def asteroids_in_sight(map, ref_y, ref_x):
    angles_set = set()
    destruction_order = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if ref_x == x and ref_y == y:
                continue
            elif map[y][x] == '#':
                angle = atan2(ref_y-y, ref_x-x) - atan2(1,0)
                angles_set.add(angle)
                if angle < 0:
                    angle = 2 * pi - abs(angle)
                destruction_order.append([x, y,
                                        sqrt((ref_x-x)**2 + (ref_y-y)**2),
                                        angle])
    return len(angles_set), destruction_order;

# main() determines asteroids in sight from best location and the 200th
# destroyed asteroid
def main():
    map = []
    max_asteroids = 0
    initial_time = time.time()

    try:
        with open("data.txt", "r") as space:
            for asteroids in space:
                map.append(asteroids.strip('\n'))

        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == '#':
                    xy_asteroids, xy_destruction = asteroids_in_sight(map, y, x)
                    if xy_asteroids > max_asteroids:
                        max_asteroids = xy_asteroids
                        max_destruction = xy_destruction

        print("Maximum asteroids in sight: ", max_asteroids)

        max_destruction.sort(key = itemgetter(3, 2))
        destroyed_asteroids = 0
        angle_index = 0
        next_angle = 1
        while True:
            while max_destruction[angle_index][3] == max_destruction[next_angle][3]:
                next_angle += 1
                if next_angle >= len(max_destruction):
                    angle_index = 0
                    next_angle = 1
            if destroyed_asteroids == 199:
                print("200th asteroid result:",
                        max_destruction[angle_index][0] * 100
                        + max_destruction[angle_index][1])
                break
            max_destruction.pop(angle_index)
            destroyed_asteroids += 1
            angle_index = next_angle - 1
            if next_angle >= len(max_destruction):
                angle_index = 0
                next_angle = 1

    except FileNotFoundError:
        print("File not found")
    except:
        print(angle_index, next_angle, len(max_destruction))
        raise

    elapsed_time = time.time() - initial_time
    print('time: {} secs'.format(elapsed_time))
    return elapsed_time

# avg_time calculates average proccesing time for the indicated number of tests
def avg_time(number_of_tests):
    return print("average time:",
                sum([main() for _ in range(number_of_tests)]) / number_of_tests)

if __name__ == '__main__':
    main()
