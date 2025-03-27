# Algorithm 1: Target Terms or Substrings

import re
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

  return output_order, output_array


# Prepare the .docx file before calling functions

doc = Document("in2a.docx")
full_text = " ".join([para.text for para in doc.paragraphs])

# Replace fancy quotes with regular quotes
normalized_text = full_text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")

# Extract the pairs of arrays using regex
array_pairs = re.findall(r'array \d+a\s*=\s*(\[".*?"\])\s*array \d+b\s*=\s*(\[.*?\])', normalized_text)

# Process each pair
with open("output_1.txt", "w") as file:
  for i, (raw_A, raw_B) in enumerate(array_pairs, start=1):
      A = eval(raw_A)  # array_A: one string inside a list
      B = eval(raw_B)  # array_B: list of city names
      output_order, output_array = find_cities_by_index(A, B)

      file.write(f"Array {i}a and {i}b:\n")
      file.write(f"Output_order = {output_order}\n")
      file.write(f"Output_array = {output_array}\n\n")

print("Results written to output_1.txt\n")
