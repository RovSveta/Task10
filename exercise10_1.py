# own function that opens, reads, converts text into a list
# and closes the file:
def text_to_list(file_to_rea):
    text = open(file_to_read)
    file_content = text.read()
    data_into_list = file_content.split("\n")
    text.close()
    return data_into_list


# defining what file to execute:
file_to_read = "artists.txt"

# printing the content of the file in a loop, line by line using own function:
print("Some of the best-selling music albums in history:\n")
for item in text_to_list(file_to_read):
    print(f"-> {item}")
