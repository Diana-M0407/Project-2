# Algorithm 1: Target Terms or Substrings

import re   #import read/write/run
from docx import Document # import document

def find_cities_by_index(array_A, array_B):
  cities = {}

  string = array_A[0]
  for city in array_B:
    index = string.find(city)
    if (index != -1):
        cities[index] = city

  sorted_cities = dict(sorted(cities.items()))

  output_order = list(sorted_cities.keys())
  output_array = list(sorted_cities.values())

  print(f"Output_order = {output_order}")
  print(f"Output_array = {output_array}")

  return output_order



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
