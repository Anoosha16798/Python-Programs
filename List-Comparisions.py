print("Welcome")
num_string=["100","98","78","56"]
num_int=[100,98,78,56]
num_float=[2.21,15.00,78.56,98.30]
num_lists=[[12,13,56],[45,36,11],[9,12,56]]
print("type of list is", type(num_string))
print("contents",num_string)
print(f"content type of {num_string[0]} is: ",type(num_string[0]))
print("type of list is", type(num_int))
print("contents", num_int)
print(f"content type of {num_int[0]} is: ", type(num_int[0]))
print("type of list is", type(num_float))
print("contents", num_float)
print(f"content type of {num_float[0]} is: ", type(num_float[0]))
print("type of list is", type(num_lists))
print("contents", num_lists)
print(f"content type of {num_lists[0]} is: ", type(num_lists[0]))
print("Now sorting\n")
num_string.sort()
print(num_string)
num_int.sort()
print(num_int)
