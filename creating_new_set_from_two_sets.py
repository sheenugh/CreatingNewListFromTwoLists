
# ----- VARIABLES -----
# - Given List
    # Given:
    # list1 = [10, 20, 25, 30, 35]
    # list2 = [40, 45, 60, 75, 90]
    # Since the two given list consist of both even numbers, I'll be creating a new two list on my own.

list1 = [10, 23, 27, 30, 31] #getting odd numbers in this list and transfer to the new list.
list2 = [40, 45, 63, 75, 91] #getting even numbers in this list and transfer to the new list.


# ------ FUNCTIONS ------
def create_new_list(list1, list2):
    new_list = []

    # Add odd numbers from the first list
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)

    # Add even numbers from the second list
    for num2 in list2:
        if num2 % 2 == 0:
            new_list.append(num2)

    return new_list


# >>>>>>>>>> PSEUDO CODE <<<<<<<<<
# ----- ACTUAL CODE -----
# - This section is for the for loop
result = create_new_list(list1, list2)
print("New or Result List = ", result)