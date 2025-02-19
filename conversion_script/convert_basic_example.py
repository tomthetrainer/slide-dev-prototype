from pathlib import Path 


# Creating a function to 
# replace the text 
def replacetext(search_text, replace_text): 

	# Opening the file using the Path function 
	file = Path(r"SampleFile.txt") 

	# Reading and storing the content of the file in 
	# a data variable 
	data = file.read_text() 

	# Replacing the text using the replace function 
	data = data.replace(search_text, replace_text) 

	# Writing the replaced data 
	# in the text file 
	file.write_text(data) 

	# Return "Text replaced" string 
	return "Text replaced"


# Creating a variable and storing 
# the text that we want to search 
search_text = "dummy"

# Creating a variable and storing 
# the text that we want to update 
replace_text = "replaced"

# Calling the replacetext function 
# and printing the returned statement 
print(replacetext(search_text, replace_text)) 
