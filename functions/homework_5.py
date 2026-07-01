
# here is a dictionary of books that I have read in 2026 with the prices
catalog = {
    'soul of desire': 15.99,
    'the great divorce': 10.99,
    'screwtape letters': 8.75,
    'killing lions': 12.78,
    'practicing the way': 17.61,
    'celebration of dicipline': 14.13,
    'project hail mary': 13.98
}

# here is the same dictionary as the last one just with dicounted prices
catalog_discount = {
    'soul of desire': 10.99,
    'the great divorce': 5.99,
    'screwtape letters': 4.75,
    'killing lions': 10.78,
    'practicing the way': 10.61,
    'celebration of dicipline': 10.13,
    'project hail mary': 9.98
}

# the example that was given for the homework assigment
catalog_example = {
    'printer paper': 6.50,
    'packing tape': 3.25,
    'shipping labels': 9.75,
    'nitrile gloves': 12.50,
    'box cutter': 4.95,
    'safety goggles': 8.25,
    'pallet wrap': 14.00
}

def build_request(catalog_arg):
  """This function will prompt the user to enter items from the argument dictionary"""
  requests = []
  while True: # the while loop will keep running
    # sets the item variable equal to the input and turns it to lower case
    item = input("Enter an item you'd like to request: ").lower()
    if item == 'submit':
      break # this ends the while loop
    elif item in catalog_arg: # checks if item is in the catalog_arg
      requests.append(item)
      print(f'{item} has been added to your request.')
    else:
      print(f'{item} is not in our catalog.')
  return requests


def calculate_subtotal(request_arg,cat_arg):
  """ takes request list and catalog dictionary displays items and price then returns subtotal"""
  subtotal = 0.0
  print('Request Summary:')
  for item in request_arg: # goes through every item in reguest_arg
    price = cat_arg[item] # finds item value in cat_arg and returns price
    print(f"{item} for ${price}") # prints results for each one
    subtotal = subtotal + price # updates subtotal
  print(f"Subtotal: ${subtotal:.2f}")
  return subtotal


def shipping_and_overhead(subtotal_arg):
  """ Calculates shipping, overhead, and final total from the subtotal_arg"""
  shipping = 15.00 # always stays the same
  overhead = 0.08 * subtotal_arg
  final_total = subtotal_arg + shipping + overhead
  return f'Shipping: ${shipping}|Overhead: ${overhead:.2f}|Final total: ${final_total:.2f}'



def main_function(catalog_arg):
  """Main function that runs all 3 functions"""
  request = build_request(catalog_arg)
  print('') # create space
  subtotal = calculate_subtotal(request,catalog_arg)
  print('') # craete space
  final_totals = shipping_and_overhead(subtotal)
  print(final_totals)



main_function(catalog_discount) # test 1

main_function(catalog) # test 2

main_function(catalog_example) # example used in homework