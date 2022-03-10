import urllib
import requests
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
import os

def nation():
    """Get article text from daily nation posts."""
    url = input("Enter post url :") # url to the post
    name = input("Enter file name :") # name of file to save scrapped text 
    decoded_string = urlopen(url).read().decode()
    my_text = BeautifulSoup(decoded_string,features="lxml").get_text()
    my_text.encode(encoding = 'UTF-8', errors = 'replace')
    sent_list = nltk.tokenize.sent_tokenize(my_text)
    content = sent_list[3:-10]
    content = ''.join(s for s in content)
    lines = content.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    clean_content = ""
    for line in non_empty_lines:
        clean_content += line + "\n"
    d_path = "C:\\Users\\MURIMI\\Desktop\\nation\\" + name
    text_file = open(d_path,'w')
    text_file.write(str(clean_content))
    text_file.close()
    print(name + ' has been saved.')
    week = input("Press Enter to exit")

nation()