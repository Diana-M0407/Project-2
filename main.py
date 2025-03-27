# c. Implement your algorithm in either Python or C++

#from docx import Document
from docx import Document


doc = Document("in2a.docx")
doc_string = " ".join([para.text for para in doc.paragraphs])


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

  print("Output_order =", output_order)
  print("Output_array =", output_array)

  return output_order                                                   # returns index values in order of appearance


find_cities_by_index(A, B)
print(doc_string)
