
data = ("Igor", "QA")

def print_person_data(firstname, lastname):
    print(firstname)
    print(lastname)


print_person_data("Igor", "QA")

# распаковка кортежа
print_person_data(*data)
print(*data)
