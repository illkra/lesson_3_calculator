
#1
#def process_strings(my_list):
    #new_list = []


    #for index, value in enumerate(my_list):
        #if index % 2 == 1:
            #new_list.append(value[::-1])
       # else:
            #new_list.append(value)

   # return new_list

#my_list = ["abc", "def", "ghi", "jkl", "mno"]
#result_list = process_strings(my_list)
#print(result_list)




#2
#def test(my_list):
    #new_list = [s for s in my_list if s[0] == "a"]
    #return(new_list)


#my_list = ["ajs", "lgkf", "plwn", "ahmsa"]
#final_list = test(my_list)
#print(final_list)



#3
#def test(my_list, char_a):
    #for char in my_list:
        #if char_a in char:
            #new_list.append(char)

    #return(new_list)


#my_list = ["ajs", "lgkfa", "plwn", "ahmsa", "fjg"]
#new_list = []
#char_a = "a"
#final_list = test(my_list, char_a)
#print(final_list)



#4
#def test(my_list):
    #new_list = [o for o in my_list if isinstance(o, str)]
    #return new_list



#my_list = ["fkalf", "gdsi", 1, 5, 7]
#sorted_list = test(my_list)

#print(sorted_list)




#5
#my_str = "gakfgakdfs"
#my_list = []

#for symbol in set(my_str):
    #if my_str.count(symbol) == 1:
        #my_list.append(symbol)

#print(my_list)





#6
#my_str_1 = "fmakfsihaslop"
#my_str_2 = "bkohfuayfukapqz"
#my_list = []

#for symbol in set(my_str_1) and set(my_str_2):
    #if my_str_1.count(symbol) and my_str_2.count(symbol) == 1:
        #my_list.append(symbol)

#print(my_list)





#7
#my_str_1 = "ggggggggggggggsqi"
#my_str_2 = "ffffffffffffgsopi"
#my_list = []

#for symbol in set(my_str_1).intersection(set(my_str_2)):
    #if my_str_1.count(symbol) < 2 and my_str_2.count(symbol) < 2:
        #my_list.append(symbol)

#print(my_list)



#8
import random
import string
from string import ascii_lowercase

def create_email(domains, names):
    name = random.choice(names)
    domain = random.choice(domains)
    number = random.randint(100, 999)

    email = f"{name}.{number}@{''.join(random.choice(ascii_lowercase) for _ in range(random.randint(5, 7)))}.{domain}"

    return email

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

e_mail = create_email(domains, names)
print(e_mail)


