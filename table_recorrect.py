# forming table function that generate a random(wrong) value at a random point in the table
import random

def wronge_func(num):

    # getting a random position for the wrong value
    pos = random.randint(2,9)

    tablenum = [i*num for i in range(1, 11)]

    # wrong value generating
    wrong_value = random.randint(1,9)

    # changing the correct value with the wrong one at pos
    tablenum[pos] += wrong_value
    return tablenum


def curerction(num, table):

    # generating correct table
    curtablenum = [i * num for i in range(1, 11)]

    for i in range(10):

        # checking each element of correct and wrong table
        if table[i] == curtablenum[i]:
            pass
        else:

            # if any element not matched . print it and its position
            print(f" The wrong value is {table[i]}  at {i+1}th position and correct value should be {curtablenum[i]}")
            print(f" correct table is {curtablenum}")

    return curtablenum

if __name__ == "__main__":

    num = int(input(" enter the num whose table you want"))

    table_num =wronge_func(num)

    print(table_num)

    (curerction(num, table_num))
