import random

# opening and reading the text file:
file = open("wisewords.txt")
content = file.read()

# converting text into a list:
text_into_list = content.split("\n")

# getting random index to get the random proverb:
max_index = len(text_into_list) - 1
random_index = random.randint(0, max_index)

# printing a random item from created list of proverbs:
print(f"Today's proverb:\n{text_into_list[random_index]}")

# close the file:
file.close()

