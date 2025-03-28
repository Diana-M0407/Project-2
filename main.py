import re     # for regex
import ast    # for safer evaluation of string literals
from docx import Document # import document


# Algorithm 1: Target Terms or Substrings
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



# Algorithm 2: Run-Length Encoding
# This function compresses any character that appears consecutively 2 or more times
# by replacing the sequence with the count followed by the character.
# Single characters are left unchanged.
def run_length_encoding(input_string):
    #Initialize an empty list to store encoded strings and char_position of input_string
    encoded_list = []     
    char_position = 0

    while char_position < len(input_string):
        #Initialize count for the current char
        count = 1

        #Count occurrences of the current char
        while char_position + 1 < len(input_string) and input_string[char_position] == input_string[char_position + 1]:
            count += 1
            char_position += 1

        #Append the encoded result
        if count > 1:
            encoded_list.append(str(count) + input_string[char_position])
        else:
            encoded_list.append(input_string[char_position])

        #Next new char in input_string
        char_position += 1

    return "".join(encoded_list)



#Extract text from docx file
def extract_text(docx_file):
  doc = Document(docx_file)
  full_text = " ".join([para.text for para in doc.paragraphs])

  #Replace fancy quotes with regular quotes
  normalized_text = full_text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")

  return normalized_text



#Extract arrays from text
def create_array_pairs(norm_text):
  # extract array pairs from .docx file
  array_pairs = re.findall(r'array \d+a\s*=\s*(\[".*?"\])\s*array \d+b\s*=\s*(\[.*?\])', norm_text)
  return array_pairs


normalized_text = extract_text("in2a.docx")
array_tuples = create_array_pairs(normalized_text)

# Process each pair of arrays
with open("output.txt", "w") as file:

  # Algorithm 1 output.txt:
  file.write(f"{'='*15} Results from Algorithm 1: \"Target Terms or Substrings\" {'='*15}\n\n")
  for i, (raw_A, raw_B) in enumerate(array_tuples, start=1):
    try:
      A = ast.literal_eval(raw_A)
      B = ast.literal_eval(raw_B)
    except(ValueError,SyntaxError) as e:
       file.write(f"Error parsing inputs on line {i}: {e}\n")
       continue

    output_order, output_array = find_cities_by_index(A, B)

    file.write(f"Input: {i}a = {raw_A}\n")
    file.write(f"       {i}b = {raw_B}\n\n")
    file.write(f"Output: Output_order = {output_order}\n")
    file.write(f"        Output_array = {output_array}\n\n\n")

  print("\nResults from Algorithm 1 written to output.txt\n")


  # Algorithm 2 output.txt:
  file.write(f"{'='*15} Results from Algorithm 2: \"Run Encoding Problem\" {'='*15}\n\n")
  for i, (raw_A, raw_B) in enumerate(array_tuples, start=1):

    long_string = run_length_encoding(raw_A)
    short_string = run_length_encoding(raw_B)

    file.write(f"Array {i}a: ")
    file.write(f"{raw_A} becomes {long_string}\n")
    file.write(f"Array {i}b: ")
    file.write(f"{raw_B} becomes {short_string}\n\n")

  print("\nResults from Algorithm 2 written to output.txt\n")
