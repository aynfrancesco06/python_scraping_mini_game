import requests
from bs4 import BeautifulSoup
from csv import DictWriter, DictReader
from random import choice

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, "html.parser")
excavated_html = soup.find_all( class_ ="quote" )

# capture author, author quote , href of author store in list
captured = [[x.find(class_ = 'text').get_text(), x.find(class_ = 'author').get_text(), x.find('a')['href']] for x in excavated_html ]
print(captured)

#capture each author data and shit
'''
author_response = requests.get('https://quotes.toscrape.com' + chosen_one[2])
soupers = BeautifulSoup(author_response.text, 'html.parser')
author_hints = [f"Author's name starts with {chosen_one[1][0]} and ends with {chosen_one[1][-1::]}", soupers.find( class_ = "author-born-date").get_text(), soupers.find( class_ = "author-born-location").get_text() ]
'''
def guess_the_auth():
    number_of_guesses = 4
    chosen_one = choice(captured)
    author_response = requests.get('https://quotes.toscrape.com' + chosen_one[2])
    soupers = BeautifulSoup(author_response.text, 'html.parser')
    author_hints = [f"Author's name starts with {chosen_one[1][0]} and ends with {chosen_one[1][-1::]}", f"Author is born on {soupers.find( class_ = 'author-born-date').get_text()}", f"Author is born in {soupers.find( class_ = 'author-born-location').get_text()}" ]
    while number_of_guesses != 0:        
        print(chosen_one[0])
        player_input = input("Guess the author: ")
        if chosen_one[1] != player_input:
            number_of_guesses -= 1
            if number_of_guesses > 0:
                print(f"You still have {number_of_guesses} guesses to go")
                print(f"Hint: {author_hints[number_of_guesses]}")
            else:
                print("No guesses for u, Game Over")
                cont = input("Do you wanna keep playing? y/n ")
                if cont == "y":
                    number_of_guesses = 4
                    chosen_one = choice(captured)
                else:
                    print("Thanks for playing")
                    break
        else:
            print ('You got it right')
            cont = input("Do you wanna keep playing? y/n ")
            if cont == "y":
                number_of_guesses = 4
                chosen_one = choice(captured)
            else:
                print("Thanks for playing")
                break


guess_the_auth()
    


#Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
#You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, 
#the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.
#Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
#After each incorrect guess, the number of guesses remaining will decrement. 
# If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
#After every incorrect guess, the player receives a hint about the author. 
#For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
#The next two hints are up to you! 
# Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.
#When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.