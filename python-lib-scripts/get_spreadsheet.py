import csv
import requests

def getGoogleSpreadsheet():
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    response.encoding = 'utf-8'
    with open("math-problem-metadata/python-lib-scripts/spreadsheet_concepts.csv", "w", newline='', encoding='utf-8') \
            as f:
        f.write(response.text)

if __name__ == '__main__':
    getGoogleSpreadsheet() # Izsauc funkciju, kas iegūst skos dokumentu CSV faila formātā
