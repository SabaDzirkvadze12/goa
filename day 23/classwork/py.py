#გადმოგეცემათ რიცხვებით სავსე სია და თქვენ უნდა დააბრუნოთ ამ სიის ელემენტების საშუალო არითმეტიკული
# def calculate_average(list):
#     total = sum(list)
#     average = total // len(list)
#     return average
# numbers = [3, 7, 11, 15, 19]
# average = calculate_average(numbers)
# print("საშულო არითმეტიკული:", average)
#გადმოგეცემათ სია რომელშიც იქნება დადებითი და უარყოფითი რიცხვებიც, თქვენ უნდა დააბრუნოთ ორი სია სადაც გაფილტრური იქნება უარყოფითი რიცხვები ცალკე და დადებითი რიცხვები ცალკე
# def filter_positive_negative(numbers):
#     positive_numbers = [num for num in numbers if num >= 0]
#     negative_numbers = [num for num in numbers if num < 0]
#     return positive_numbers, negative_numbers
# numbers = [1, -2, -3, 1, 2, 3]
# positive, negative = filter_positive_negative(numbers)
# print("დადებითი რიცხვები:", positive)
# print("უარყოფითი რიცხვები:", negative)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("პირველი სამი ელემენტი:", nums[:3])
print("ბოლო სამი ელემენტი:", nums[-3:])
print("ელემენტები ინდექსიდან 3-დან 7-მდე:", nums[3:8])
print("მთლიანი სია:", nums)

sentence =  ["gamarjoba,", "rogor", "xar", "dges?"]