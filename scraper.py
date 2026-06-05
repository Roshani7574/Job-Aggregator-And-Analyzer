import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

keyword = input("Enter job keyword: ").lower()

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Job Title", "Company", "Location"])

    for job in jobs:

        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p", class_="location").text.strip()

        if keyword in title.lower():

            print("\nJob Found!")
            print("Title:", title)
            print("Company:", company)
            print("Location:", location)

            writer.writerow([title, company, location])