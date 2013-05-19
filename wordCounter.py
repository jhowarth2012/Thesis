"""
Script to read only main body text from a latex source file, discards all mark up.
Takes file to be counted as command line argument, prints total count on command line
Steven #### 8/4/13
"""

from sys import argv

# Sets a list of key words that latex uses for formating

keywords = ['\\begin',
            '\\end',
            '\\section',
            '\\subsection',
            '\\usepackage',
            '\\hline',
            '\\caption',
            '\\lipsum',
            '\\label',
            '\\\\',
            '\r\n',
            '\\item',
            '\\textbf',
            '\\textit',
            '\\emph',
            '\\',
            '[',
            ']',
            '{',
            '}',
            '&',
            ]

# recursive flatten function, takes a nested list, returns 1D list
def flatten(nested_num_list):
	flat_list = []
	for item in nested_num_list:
		if type(item) == type([]):
			flat_list += flatten(item)
		else:
			flat_list.append(item)
	return flat_list



#Function takes a list of strings and outputs a list of words. Traverses list, uses string.split() on each entry in the list
def text_breaker(list_of_strings):
    new_list = []    
    for line in list_of_strings:
        new_list.append(line.split()) #This works but not when '--' is in the text
    return flatten(new_list)


# Function check to see if word is in key list 
def keyword_filter(word):
    for keyword in keywords:
        if word.startswith(keyword) or word.endswith(keyword):
            return True    
    return False    

# Open specified file
infile_name = argv[1]
infile = open(infile_name, 'r')

# Pass list of lines to text var
text = infile.readlines()

#close file
infile.close()

#list of words, includes punctuation and keywords
text = text_breaker(text)

clean_list = []

#traverse list, add element if not from keyword list

skip    = False
skip = False

for item in text:
    if ("\\begin{table}" in item or "\\begin{graphics}" in item):
        skip = True
    if (item == "\\end{table}" or item == "\\end{graphics}"):
        skip = False
    if skip:
        continue
    if keyword_filter(item) == False:
        clean_list.append(item)

#print word count
if len(infile_name)>15:
	print "File: ",infile_name,"\t Words = ",len(clean_list)
else:
	print "File: ",infile_name,"\t\t Words = ",len(clean_list)
