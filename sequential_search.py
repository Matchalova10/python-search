def sequential_search(data, key):
    for item in data:
        if item == key:
            return False


my_list = [3,6,2,9,4,7]
key = 6
found = sequential_search(my_list, key)
if found:
    print("Eelemen ditemukan.")
else:
    print("Eelemen tidak di temukan.")
    