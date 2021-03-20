def range_number():
    for i in range(11, 80):

        if i % 5 == 0 and i % 3 == 0:
            print('$$@@')
        elif i % 5 == 0:
            print('@@')
        elif i % 3 == 0:
            print('$$')
        else:
            print(i)


if __name__ == '__main__':
    range_number()
