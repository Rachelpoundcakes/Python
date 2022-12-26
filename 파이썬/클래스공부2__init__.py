# 매직 메소드 __init__ 사용하여 만들어보기

class Book(object):
    count = 0

    def __init__(self, author, title, publisher, date):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        Book.count += 1
    
    def print_info(self):
        print("Author: ", self.author)
        print("Title: ", self.title)
        print("Publisher: ", self.publisher)
        print("Date: ", self.date)

book = Book("니시오 히로카즈", "코딩을 지탱하는 기술", "BJ", "2013")

book.print_info()
print("Number of Books: ", str(Book.count))

"""
결과
Author:  니시오 히로카즈
Title:  코딩을 지탱하는 기술
Publisher:  BJ
Date:  2013
Number of Books:  1
"""