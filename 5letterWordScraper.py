from bs4 import BeautifulSoup
import requests
import re

word_list = []
for i in range(28):

    if(i == 0):
        #first page URL has a different link (slightly)
        url = "https://www.bestwordlist.com/5letterwords.htm"
    else:
        url = f"https://www.bestwordlist.com/5letterwordspage{i-1}.htm"

    # get the info
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract text content from HTML
    text = soup.get_text()
    #find the first occurence of 5 cpaital letters next to eachother
    match = re.search(r'[A-Z]{5}', text)
    matches = list(re.finditer(r'[A-Z]{5}', text))

    #used -2 since there was an extra occurence after the words had been listed for each page
    last_match = matches[-2]
    text = text[match.start():last_match.start()+5]

    # Split the text into individual words and add to the list
    words = text.split()
    for word in words:
        word_list.append(word.lower())

# Write the words to a text file
with open("5words.txt", "w") as file:
    for word in word_list:
        file.write(word + "\n")