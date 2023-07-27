import requests
from bs4 import BeautifulSoup

def scrape_openai_blog():
    url = "https://openai.com/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h2").text.strip()
        link = url + article.find("a")["href"]
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)
import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_the_number()

class CentralLock:
    def __init__(self):
        self.is_locked = False
    
    def lock(self):
        if self.is_locked:
            print("The central lock is already locked.")
        else:
            self.is_locked = True
            print("The central lock is now locked.")
    
    def unlock(self):
        if not self.is_locked:
            print("The central lock is already unlocked.")
        else:
            self.is_locked = False
            print("The central lock is now unlocked.")

# Create an instance of the CentralLock class
lock = CentralLock()

# Demonstration of locking and unlocking
lock.lock()  # Output: The central lock is now locked.
lock.unlock()  # Output: The central lock is now unlocked.
lock.unlock()  # Output: The central lock is already unlocked.
lock.lock()  # Output: The central lock is now locked.


scrape_openai_blog()
import requests
from bs4 import BeautifulSoup

def scrape_openai_blog():
    url = "https://openai.com/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h2").text.strip()
        link = url + article.find("a")["href"]
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)

scrape_openai_blog()
import requests
from bs4 import BeautifulSoup

def scrape_openai_blog():
    url = "https://openai.com/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h2").text.strip()
        link = url + article.find("a")["href"]
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)

scrape_openai_blog()
import requests
from bs4 import BeautifulSoup

def scrape_openai_blog():
    url = "https://openai.com/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h2").text.strip()
        link = url + article.find("a")["href"]
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)

scrape_openai_blog()
import requests
from bs4 import BeautifulSoup

def scrape_openai_blog():
    url = "https://openai.com/blog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h2").text.strip()
        link = url + article.find("a")["href"]
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)

scrape_openai_blog()
