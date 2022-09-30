# Определить, присутствует ли в заданном списке строк, некоторое число
str1 = ['воп23', 'д1ы', '56', 'ьу', '0', '8', 'ло765п', '2', 'вк']
# def find_digit(new_text):
#     for i in range(len(new_text)):
#         if new_text[i].isdigit():
#             print(i)

# find_digit(str1)

def find_digit(new_text, num):
    for i in range(len(new_text)):
        if new_text[i].isdigit():
            if int(new_text[i]) == num:
                print(i)
find_digit(str1, num)

