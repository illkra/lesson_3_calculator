
#1
#def read_domains_from_file(file_name):
        #with open(file_name, 'r') as file:
         #   domains = [line.strip() for line in file]
          #  domains = [domain.replace('.', '') for domain in domains]

     #   return domains


#file_name = "domains.txt"
#result = read_domains_from_file(file_name)

#print(result)




#2

#def names_from_files(file_name):
#    with open(file_name, 'r') as file:
#        lines = [line.strip() for line in file]
#        surnames = [line.split('\t')[1] for line in lines]

 #       return(surnames)


#file_name = "names.txt"
#result = names_from_files(file_name)
#print(result)





#3
import re

def extract_dates_from_file(file_name):
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file]

        date_pattern = re.compile(r'\b(\d{1,2}(st|nd|rd|th) [a-zA-Z]+ \d{4})\b')

        dates = [{"date": match.group(1)} for line in lines for match in date_pattern.finditer(line)]

        return dates

file_name = "authors.txt"
result = extract_dates_from_file(file_name)

print(result)
