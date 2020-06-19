import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.nytimes.com/books/best-sellers/series-books/'

book_list = []


def check_book_list():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    books_area = soup.find_all('div', {'class': 'css-xe4cfy'})
    for index in range(0, len(books_area)):
        if len(book_list) > 9:
            break
        title = books_area[index].select('h3.css-5pe77f')[0].text
        book_list.append(title)
    print(book_list)
    send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('stayhome726@gmail.com', '1110597219')
    all_books = ''
    increment = 1
    for book in book_list:
        all_books = all_books + f"{increment}.  " + book + "\n"
        increment += 1
    subject = 'Bestseller children\'s books !'
    body = f'Top 10 Bestseller children\'s series on \'The New york Times\'---> {URL}\n' + all_books
    massage = f"Subject : {subject}\n\n{body}"
    server.sendmail(
        'satyhome726@gmail.com',
        'atmahad726@gmail.com',
        massage
    )
    print('Hey email has been sent!')
    server.quit()


check_book_list()
