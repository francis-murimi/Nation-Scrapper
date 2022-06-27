""" This python file can be run as a script.
It can be run on the terminal or as an executable program."""
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

def scrapper():
    """
    Handling requests.
    Processing web page to get text.
    Saving scrapped text to a file. """
    # Welcome greetings
    print('Running scrapper for Nation.africa, TowardsDataScience.com and NewYorkTimes.com')
    print('Welcome to chaos!')
    # Start of request handling
    url = input('Enter the url of webpage you wish to scrap : ') # Provide url
    fileName = input('Enter name of file to save scrapped text in : ') # Provide file name only and not type
    name = fileName + '.txt' # Add a txt file fomart explicitly
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # Parse headers for server to grant authorization for HTML reading
    webpage = urlopen(req).read()
    page_soup = soup(webpage,"html.parser") # Beautifulsoup
    text = page_soup.find_all('p')
    content = '\n\n'.join(p.text for p in text) # finish processing text
    # File opening and saving
    d_path = "C:\\Users\\MURIMI\\Desktop\\nation\\" + name # Path to store the saved file
    text_file = open(d_path,'w') # open text file
    text_file.write(content) # write text that has been formated into paragraphs
    text_file.close() # close the opened text file
    print(name + ' has been saved.') # show scrapping is complete
    contvariable = input("Press 1 to continue or Press 2 to exit scrapper : ") # Enter option to continue scrapping or exit
    if int(contvariable) == 1: # loop the function if needed to save time
        scrapper()
    elif int(contvariable) == 2:
        print('Thank you for using my scrapper. Nice time till next time.')
        the_end = input('Press enter to exit')

scrapper()