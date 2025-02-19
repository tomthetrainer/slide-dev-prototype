from pathlib import Path
import re 


# Creating a function to 
# replace the text 
def replacetext(search_text, replace_text): 

	# Opening the file using the Path function 
	file = Path(r"fixed.txt")
	file_to_write = Path(r"fixed2.txt") 

	# Reading and storing the content of the file in 
	# a data variable 
	data = file.read_text() 

	# Replacing the text using the replace function 
	data = re.sub(search_text, replace_text, data) 

	# Writing the replaced data 
	# in the text file 
	file_to_write.write_text(data) 

	# Return "Text replaced" string 
	return "Text replaced"


# text = "The cat sat on the mat."
# pattern = r"cat"
# replacement = "dog"
# new_text = re.sub(pattern, replacement, text)
# print(new_text)

# Creating a variable and storing 
# the text that we want to search 
search_text = r"<.*?>"

# Creating a variable and storing 
# the text that we want to update 
replace_text = ""



# Calling the replacetext function 
# and printing the returned statement 
print(replacetext(search_text, replace_text)) 
	
