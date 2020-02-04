# This program reads in a string
# and strips any leading or trailing spaces.
# It also converts all the letters to lower case.
#This program also informs the user whats the length
#original string and of the normalised one

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalisedString = len(normalisedString)

print("That string when normalised is: {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalisedString))

