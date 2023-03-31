def save_to_file(filename, my_arr):
    with open(filename, 'a') as f:
        for value in my_arr:
            f.write(str(value)+'\n')


def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        arr = []
        for i in lines:
            arr.append(i[:-1])
        new_array = [arr[i:i + 3] for i in range(0, len(arr), 3)]
    except:
        new_array = []
    return new_array


if __name__ == "__main__":
    save_to_file('db.txt', ['title3', 'description3', 7])
    print(read_from_file('db.txt'))