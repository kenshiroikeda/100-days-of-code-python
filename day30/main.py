# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     a_dictionary["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
# finally:
#     file.close()
#     print("file was closed.")
# # a_dictionary = {"key": "value"}
# # a_dictionary["non_key"]
#
# # fruit_list = ["apple","banana","pear"]
# # fruit_list[3]
#
# #text = "abc"
# #print(text + 3)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)