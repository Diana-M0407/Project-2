# c. Implement your algorithm in either Python or C++

import re   #import read/write/run
from docx import Document # import document

#Input:
A = [ "thismetoaklandrialtofullertonmarcolongchinofresnovallejoclovissimithound"]
B = [ 'marco', 'clovis', 'rialto', 'oakland']

#Docx:
array_1a = ["sanoaklandrialtofullertonmarcolongbreacoronamodestoclovissimithousand"]
array_1b = ['brea', 'modesto', 'clovis', 'corona']


array_2a = ["marcopolmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas"]
array_2b = ['fullerton', 'chino', 'fremont', 'fresno']

array_3a = ["torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange"]
array_3b = ['oxnard','irvine', 'orange', 'marco']


def find_cities_by_index(array_A, array_B):
  cities = {}

  # m = length of array_A
  # n = length of array_B
  # s = number of characters of string, array_A[0]

  string = array_A[0]
  for city in array_B:                                                  # ----> Efficiency Class:  O(m) - "Linear"
    index = string.find(city)                                           # ----> Efficiency Class:  O(s) - "Linear"
    if (index != -1):
        cities[index] = city


  sorted_cities = dict(sorted(cities.items()))                          # -----> Efficiency Class: k log k - "Logarithmic"

  output_order = list(sorted_cities.keys())
  output_array = list(sorted_cities.values())

  print(f"Output_order = {output_order}")
  print(f"Output_array = {output_array}")

  return output_order                                                   # returns index values in order of appearance



# Prepare the .docx file before calling functions
doc = Document("in2a.docx")
doc_string = " ".join([para.text for para in doc.paragraphs])

# Replace fancy quotes with regular quotes
normalized_text = doc_string.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")

# Extract the pairs of arrays using regex
array_pairs = re.findall(r'array \d+a\s*=\s*(\[".*?"\])\s*array \d+b\s*=\s*(\[.*?\])', normalized_text)

# Process each pair
for i, (raw_A, raw_B) in enumerate(array_pairs, start=1):
    A = eval(raw_A)  # array_A: one string inside a list
    B = eval(raw_B)  # array_B: list of city names
    print(f"\n▶ Matching array {i}a and {i}b")
    find_cities_by_index(A, B)

