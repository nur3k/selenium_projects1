def count_backwards():
    for i in range(100, 0, -1):
        if i % 5 == 0 and i % 3 == 0:
            print("Testing")
            continue
        elif i % 3 == 0:
            print("Software")
            continue
        elif i % 5 == 0:
            print("Agile")
            continue
        else:
            print(i)


count_backwards()
