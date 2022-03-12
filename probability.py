import numpy as np
from matplotlib import pyplot as plt


def roll_dice():
    general_list = np.arange(0)
    for iterator in range(5):
        dice_list = np.arange(1, 7)
        np.random.shuffle(dice_list)
        general_list = np.append(general_list, dice_list[0])
    return general_list


def roll_dice_for_conditional():
    general_list = np.arange(0)
    even_parts = None
    for iterator in range(4):
        dice_list = np.arange(1, 7)
        even_parts = np.array([2, 4, 6])
        np.random.shuffle(dice_list)
        np.random.shuffle(even_parts)
        general_list = np.append(general_list, dice_list[0])
    general_list = np.append(general_list, even_parts[0])
    print(general_list)
    return general_list


def probability1_2(data_list):
    return 3 in data_list


def probability3(data_list):
    if 3 in data_list:
        even_counter = 0
        for even_checker in data_list:
            if even_checker % 2 == 0:
                even_counter += 1
        if even_counter > 1 or even_counter == 0:
            return False
        else:
            return True
    else:
        return False


def roll_dice_multiple(experiment_parameter):
    N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    for iterator in N:
        counter1 = 0
        array1 = np.arange(0)
        for looper_var in range(iterator):
            if experiment_parameter == 1:
                plt.axhline(y=59.812, color='r', linestyle=':')
                booler = probability1_2(roll_dice())
            elif experiment_parameter == 2:
                plt.axhline(y=52.953, color='g', linestyle=':')
                booler = probability1_2(roll_dice_for_conditional())
            elif experiment_parameter == 3:
                plt.axhline(y=12.037, color='b', linestyle=':')
                booler = probability3(roll_dice())
            else:
                booler = None
                exit(1)
            if booler:
                counter1 += 1
            array1 = np.append(array1, (counter1 / (looper_var + 1)) * 100)

        plt.plot(np.arange(iterator), array1)
        plt.show()


roll_dice_multiple(3)
