import urllib
import requests
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
import os

def nation():
    """Get article text from daily nation posts."""
    url = input("Enter post url :") # prompt for url to the post
    name = input("Enter file name :") # prompt for name of file to save scrapped text 
    decoded_string = urlopen(url).read().decode() # convert bytes to str
    my_text = BeautifulSoup(decoded_string,features="lxml").get_text() # get the text from html and javascript
    my_text.encode(encoding = 'UTF-8', errors = 'replace') # use UTF-8 encoding.
    sent_list = nltk.tokenize.sent_tokenize(my_text) # split text into sentences
    content = sent_list[3:-10] # get the sentences that are commonly unique for each post
    content = ''.join(s for s in content) # combine the sentences
    # separate and join lines to form paragraphs
    lines = content.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    clean_content = ""
    for line in non_empty_lines:
        clean_content += line + "\n"
    # end of paragraphing
    d_path = "C:\\Users\\MURIMI\\Desktop\\nation\\" + name # path to where the text file will be saved at
    text_file = open(d_path,'w') # open text file
    text_file.write(str(clean_content)) # write text that has been formated into paragraphs
    text_file.close() # close the opened text file
    print(name + ' has been saved.') # show scrapping is complete
    endvariable = input("Press Enter to exit") #Find assurance by closing python.exe yourself

nation() # call the scrapping function