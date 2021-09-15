import re #regular expression module
#regular expressions are descriptions for a pattern of text
#'\d' - digit, '\D'- any character thats not a digit,'\w' - alphanumeric , 
# '\s'- space character, '\S'- any character that isnt a space
#'{}' - curly brackets matches specific repititions
#'.compile()' - returns a RegEx object
#'.search()' - searches the string it is passed for any matches to the regex
#'group()' - returns the matched text
#'()'- group expression with parenthesis, '*' - characters repeated zero or more times,
# '+' - characters repeated at least once, '|' - matches multiple groups, '?'- optional matching
#'.findall()'- return strings of every match 
#'^' - a match must occur at the beginning, '$'- a match must occir at the end, 
# '.'- matches any character expect a new line
#Examples:
phoneRegEx = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneRegEx.search("my phone number is 415-555-7891")
print("Phone number found: " + mo.group())
cerealsRegEx = re.compile(r'Trix|Cheerios')
mat = cerealsRegEx.findall(" Trix and Cheerios")
print(mat)