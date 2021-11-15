# JSON: Javascript Object Notation
# -> Light Weight file used for data
# interchange.
# -> Generally involves nested
# structure of list and dict.
# {key: value} and here:-
# Values can be:-
# 	String
# 	Number(int and float)
# 	Another JSON Object
# 	Array(List)
# 	bool
# 	null(None)

# fp = open('fruits.json','r')
# content = fp.read()
# print(type(content))
# print(content)

# import json
# dict_content = json.loads(content)
# print(type(dict_content))
# print(dict_content)

# print(dict_content.keys())
# print(dict_content['apple'])

# fp = open('space_astro.json','r')
# content = fp.read()
# import json
# dict_content = json.loads(content)

# print(dict_content.keys())
# for person in dict_content['people']:
# 	print(person['name'])

# Q1) Write names of all the astronauts whose craft name is starting from
# 'f'

# fp = open('space_astro.json','r')
# content = fp.read()
# import json
# dict_content = json.loads(content)
# for person in dict_content['people']:
# 	if person['craft'][0] == 'f':
# 		print(person['name'])

# Creating a json file from dict.
# dict1 = {"Aditya":"Yadav",'C++':14,'C#':3}
# import json
# dump_data = json.dumps(dict1)
# fp = open('aditya.json','w+')
# fp.write(dump_data)
# fp.close()


# XML Files:
# - Extensible Markup Language
# - Used for Sending and Receiving Data
# - They look like html, but the don't have have predefined tags like div,a,b,h,etc
# - You make your own tags, You make tags to specify what data you are
# storing.

# {"apple": 4, "mango": 5}

# <fruits>
# 	<fruit>
# 		<name>apple</name>
# 		<count>4</count>
# 	</fruit>
# 	<fruit>
# 		<name>mango</name>
# 		<count>5</count>
# 	</fruit>
# </fruits>

# Rules for XML Files:
# 1) Opening and Closing tags should be same.
# 2) There should be a Root tag
# 3) Case Sensitive

# python Vs Python Vs PYTHON Vs PyTHon All these are different.

# from bs4 import BeautifulSoup
# with open('test_file.xml','r') as fp:
#     soup = BeautifulSoup(fp,'html.parser')

# print(soup)
# print(type(soup))

# print('----------Waffles ka Dhaba------------')
# food_list = soup.find_all('food')
# for food in food_list:
#     print(food.find('name').text,food.find('price').text)

# CSV:COMMA SEPARATED VALUES

# import csv

# with open('test.txt') as fp:
#     csv_reader = csv.reader(fp,delimiter=',')
#     print(type(csv_reader))
#     for row in csv_reader:
#         print(row)

# - They are important to store the data in a table like format.
# - We can make a table directly from a csv file using pandas, and many other
# libraries
# - excel,xlsx, spreadsheets files are very similar to csv and you can convert
# them into each other.
# - Generally Top first line contains the name of the columns or heading.
# -csv files are created by programs that handle huge amount of data.