#1

#number = 4124912049250129050
#count_zeroes = str(number).count("0")

#print(number)
#print(count_zeroes)


#2

#my_number = 1000000000000200000
#count_zeros = 0

#while my_number % 10 == 0:
 #   count_zeros += 1
 #   my_number //= 10

#print(count_zeros)



#3
#my_list_1 = [0, 1, 2, 3, 4, 5]
#my_list_2 = [0, 10, 20, 30, 40, 50]
#my_result = []

#for i in my_list_1:
    #if i % 2 == 0:
     #my_result.append(my_list_1[i])

#my_result.extend([my_list_2[i] for i in range(len(my_list_2)) if i % 2 == 0])

#print(my_result)



#4
#my_list = [1, 2, 3, 4, 5]
#new_list = my_list[1:]
#new_list.append(my_list[0])

#print(new_list)




#5
#my_list = [1, 2, 3, 4, 5]
#removed_number = my_list.pop(0)
#my_list.append(removed_number)

#print(my_list)





#6
#my_string = "19 is more than 8 but lower than 36"

#numbers = [int(element) for element in my_string.split() if element.isdigit()]
#total_sum = sum(numbers)

#print(total_sum)




#7
#my_list = [1, 6, 3, 8, 5, 10, 1]

#count = 0

#for i in range(len(my_list) - 1):
    #if my_list[i] > my_list[i - 1] + my_list[i + 1]:
        #count += 1

#print(count)





#8
#my_list = [1, 2, 3, "4", "5", "6"]
#new_list = []

#for i in my_list:
    #if isinstance(i, str):
        #new_list.append(i)

#print(new_list)




#9
#my_str = "abaksfaslcasfaks"
#my_list = []

#my_list.append(set(my_str))

#print(my_list)




#10
#string_1 = "fagsokcd"
#string_2 = "1528543"
#my_list = []

#for char in string_1:
    #my_list.append(char)

#for char in string_2:
    #my_list.append(char)

#print(my_list)





#11
#string_1 = "51254124"
#string_2 = "58199421"

#set_1 = set(string_1)
#set_2 = set(string_2)

#same = set_1.intersection(set_2)

#print(same)

