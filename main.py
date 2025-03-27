# c. Implement your algorithm in either Python or C++

from docx import Document


doc = Document("in2a.docx")
doc_string = " ".join([para.text for para in doc.paragraphs])

array_1a = ["sanoaklandrialtofullertonmarcolongbreacoronamodestoclovissimithousand"]
array_1b = ['brea', 'modesto', 'clovis', 'corona']


array_2a = ["marcopolmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas"]
array_2b = ['fullerton', 'chino', 'fremont', 'fresno']

array_3a = ["torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange"]
array_3b = ['oxnard','irvine', 'orange', 'marco']

#Input:
A = [ "thismetoaklandrialtofullertonmarcolongchinofresnovallejoclovissimithound"]
B = [ 'marco', 'clovis', 'rialto', 'oakland']

#Output: Output_order = [ 7, 14, 29, 56]
#Output_array =[ ‘oakland’, ‘rialto’, ‘marco’, ‘clovis’]


def find_cities_by_index(array_A, array_B):
  cities = {}

  # m = length of array_A
  # n = length of array_B
  # s = number of characters of string, array_A[0]


  '''
  # if arrya_A had more than one string
  for city in array_B:                                                  # ----> Efficiency Class:  O(m) - "Linear"
    for s in array_A:                                                   # ----> Efficiency Class:  O(n) - "Linear"
      index = s.find(city)
      if (index != -1):
        cities[index] = city
  '''


  string = array_A[0]
  for city in array_B:                                                  # ----> Efficiency Class:  O(m) - "Linear"
    index = string.find(city)                                           # ----> Efficiency Class:  O(s) - "Linear"
    if (index != -1):
        cities[index] = city


  sorted_cities = dict(sorted(cities.items()))                          # -----> Efficiency Class: k log k - "Logarithmic"

  output_order = []
  output_array = []
  for idx, val in sorted_cities.items():                                # ---->Efficiency Class: O(k) - "Linear"
    output_order.append(idx)
    output_array.append(val)


  print(f"Output_order = {output_order}\n")
  print(f"Output_array = {output_array}\n")

  return output_order                                                   # returns index values in order of appearance


find_cities_by_index(A, B)
find_cities_by_index(array_1a, array_1b)
find_cities_by_index(array_2a, array_2b)
find_cities_by_index(array_3a, array_3b)
#print(doc_string)
