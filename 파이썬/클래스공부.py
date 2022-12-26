# 클래스의 기능: attribute, method, instance

# Book으로 클래스 만들어보기

class Book(object):
    author = ""
    title = ""
    publisher = ""
    date = ""
    count = 0

    def print_info(self):
        print("Author: ", self.author)
        print("Title: ", self.title)
        print("Publisher", self.date)
    
book = Book()
Book.count += 1
book.author = "니시오 히로카즈"
book.title = "코딩을 지탱하는 기술"
book.publisher = "BJ"
book.date = "2013"

book.print_info()
print("Number of Books: ", str(Book.count))

"""
결과
Author:  니시오 히로카즈
Title:  코딩을 지탱하는 기술
Publisher 2013
Number of Books:  1
"""

