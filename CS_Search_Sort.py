# Insertion Sort
array = [8, 2, 10, 1, 4, 9, 3]
temp = 0
print("Not Ordered: ", array)
for i in range(1, len(array)):
    temp = array[i]
    while i > 0 and array[i] < array[i-1]:
        array[i] = array[i - 1]
        i = i-1
        array[i] = temp

print(array)

# Binary Search
search = int(input("Enter number to be found: "))
lower = 0
upper = len(array)
fail = False
found = False
while not found and not fail:
    middle = int((lower+upper)/2)
    if search == array[middle]:
        found = True
        print("Found at Index: ", middle)
    elif lower >= upper:
        fail = True
        print("Not Found")
    elif search <= array[middle]:
        upper = middle-1
    elif search >= array[middle]:
        lower = middle+1
