

#  a. Develop  a  complete  and  clear  pseudocode  for  an  algorithm  to  solve  this  problem.
#     Your algorithm should return the indices of the target words (contents of array B) in
#     ascending  order  of  their  appearance  in  array  A.  It  should  also  print  the  words,
#     according to the resulting order of appearance.

'''

  # PSEUDOCODE for part a algorithm:

  function find_cities_by_index(strings_A, cities_B):
      # Create a dictionary to store index: city pairs
      city_map = {}

      for city in cities_B:
          if city is in strings_A:
              index = starting position of city in strings_A
              city_map[index] = city  # store in dictionary

      # Sort dictionary items by index (keys)
      sorted_city_map = city_map sorted by key in ascending order

      output_order = []
      output_array = []

      for each (index, city) in sorted_city_map:
          append index to output_order
          append city to output_array

      print output_array
      return output_order

'''


'''
######################### b. Mathematically analyze your pseudocode and state the efficiency class ###################################

def find_cities_by_index(array_A, array_B):
  cities = {}

  # m = length of array_A
  # n = length of array_B
  # s = number of characters of string, array_A[0]



  # # if arrya_A had more than one string
  # for city in array_B:                                                  # ----> Efficiency Class:  O(m) - "Linear"
  #   for s in array_A:                                                   # ----> Efficiency Class:  O(n) - "Linear"
  #     index = s.find(city)
  #     if (index != -1):
  #       cities[index] = city



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


'''





####################################  c. Implement your algorithm in either Python or C++ ################################

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
