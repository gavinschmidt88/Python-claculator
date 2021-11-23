# first we need to open the name file so we know what the names of the children are
childrens_names_file = open("childrensNames.txt", "r")

# create or append to a file the names of absent children we need to read from this file later
absent_file = open("absent.txt", "a+")
# create a variable to store the cursors starting position
starting_position_absent_file = absent_file.tell()

# ask the user for todays date
date = input("What is today's date? (dd/mm): ")

# for every name in the list of names ask whether that chils is present
for name in childrens_names_file:
  name = name.rstrip(name[-1])
  present = input("Is " + name + " present? (y/n): ")

  # if not add an entry to the absent file with the date
  if present == "n" or present == "N":
    absent_file.write(name + " absent on (" + date + ")\n")

# close the name file now we're done with it
childrens_names_file.close()

# go back to the starting position
absent_file.seek(starting_position_absent_file)

# tell the user we are about to print all new entries
print("\n\n\nNew entries to absent file:\n")

# print all new entries
print(absent_file.read())

# close the absent file since we're done
absent_file.close()