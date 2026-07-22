def save_data(obj, filename):
  '''This function is. used for saving the input dictionary file into the the file for data entry.'''
  import csv
  if filename:
    #open file using with for automatic closing after use
    with open(filename, 'r+', newline='') as file:
      writer=csv.writer(file)
      char=file.read(1)
      if not char:
        writer.writerow(obj.keys())
      writer.writerow(obj.values())
      
  return "Invalid filename"


def read_data(filename):
  
  '''This function will be used to read the file data to display the written data.'''
  import csv
  l=[]
  if filename:
    #open file using with for automatic closing after use
    with open(filename, 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
        l.append(row)
    return l
  return "Invalid filename"


