#1

#my_list = ["abc", "def", "ghi", "jkl", "mno"]

#new_list = []

#for index, value in enumerate(my_list):
    #if index % 2 == 1:
        #new_list.append(value[::-1])
    #else:
        #new_list.append(value)

#print(new_list)






#2

#my_list = ["apple", "banana", "orange", "grape", "avocado"]

#new_list = []

#for value in my_list:
    #if value.startswith("a"):
        #new_list.append(value)

#print(new_list)




#3

#my_list = ["apple", "banana", "orange", "grape", "avocado"]

#new_list = []

#for value in my_list:
    #if "a" in value:
        #new_list.append(value)

#print(new_list)




#4
#a
#people = [{"name": "John", "age": 15}, {"name": "Jane", "age": 20}, {"name": "Jack", "age": 15}]
#min_age = min(person["age"] for person in people)
#youngest_names = [person["name"] for person in people if person["age"] == min_age]
#print("youngest:", youngest_names)
#b
#people = [{"name": "John", "age": 15}, {"name": "Jane", "age": 20}, {"name": "Jack", "age": 15}]
#max_name_length = max(len(person["name"]) for person in people)
#longest_names = [person["name"] for person in people if len(person["name"]) == max_name_length]
#print("longest names:", longest_names)
#c
#people = [{"name": "John", "age": 15}, {"name": "Jane", "age": 20}, {"name": "Jack", "age": 25}]
#average_age = sum(person["age"] for person in people) / len(people)
#print("average age:", average_age)



#5
#a
#my_dict_1 = {"a": 1, "b": 2, "c": 3}
#my_dict_2 = {"b": 20, "c": 30, "d": 40}

#common_keys = [key for key in my_dict_1.keys() if key in my_dict_2]

#print("both dict keys:", common_keys)

#b
#my_dict_1 = {"a": 1, "b": 2, "c": 3}
#my_dict_2 = {"b": 20, "c": 30, "d": 40}

#unique_keys = [key for key in my_dict_1.keys() if key not in my_dict_2]

#print("unique keys in first dict:", unique_keys)

#c
#my_dict_1 = {"a": 1, "b": 2, "c": 3}
#my_dict_2 = {"b": 20, "c": 30, "d": 40}

#new_dict = {key: my_dict_1[key] for key in my_dict_1.keys() if key not in my_dict_2}

#print("new dict:", new_dict)

#d
my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}

merged_dict = {}

for key, value in my_dict_1.items():
    if key not in my_dict_2:
        merged_dict[key] = value

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        merged_dict[key] = value

for key in set(my_dict_1.keys()).intersection(my_dict_2.keys()):
    merged_dict[key] = [my_dict_1[key], my_dict_2[key]]

print("merged dict:", merged_dict)

