import re
def digit_to_text(digit):
    digit_dict = {'0':"ноль",'1':'один','2':'два',
                '3':'три','4':'четыре','5':'пять',
                '6':'шесть','7':'семь'}
    return digit_dict.get(digit)
k=1
with open("text.txt","r") as file:
    data = file.read()
    regul ="\d{1,5}[1357]"
    numbers = re.findall(regul, data)
    for number in numbers:
        if int(len(number)) % 2 == 0 and int(len(number)) > k:
            for i in number:
                print(digit_to_text(i), end = " ")
            print(" ")
            
