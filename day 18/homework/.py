# # def fuction(numbers):
# #     for i in range(20):
# #       print(i)
# # print(fuction)

# # def add_name_to_list():
# #     names_list = []

# #     first_name = input("Enter your first name: ")

# #     last_name = input("Enter your last name: ")

# #     names_list.append(first_name)
# #     names_list.append(last_name)

# #     print("Names list:", names_list)

# # def filter_list(start_num,end_num):
# #     filtered_list = []
# #     for i in range(start_num,end_num):
# #         if i % 2 == 0:
# #             filtered_list.append(i ** 2)
# #         else:
# #             filtered_list.append(i ** 0.5)
# #     return filtered_list
# # start_num = int(input("Please enter first number: "))
# # end_num = int(input("Please enter second number: "))
# # result_list = filter_list(start_num,end_num)
# # print(result_list)


# def even_indexes(lastname):
#     char_list = []
#     even_index_chars = []
#     for char in lastname:
#         char_list.append(char)
#     for index in range(len(char_list)):
#         if index % 2 == 0:
#             even_index_chars.append(char_list[index])
#     return even_index_chars
# lastname = input("Please enter lastname: ")
# print(even_indexes(lastname))