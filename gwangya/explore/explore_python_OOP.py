 #Note를 정리하는 프로그램
 #사용자는 Note에 무엇인갈 적을 수 있다
 #Note에는 Content가 있고, 내용을 제거할 수 있다
 #두 개의 노트북을 합쳐 하나로 만들 수 있다
 #노트는 노트북에 삽입된다
 #노트북은 노트가 삽입될 때 페이지를 생성하며, 최고 300페이지
 #300페이지가 넘으면 더 이상 노트를 삽입하지 못 한다

 #노트북과 노트의 속성과 메소드에 대해서 먼저 생각해보자
 #Notebook_method : add_note, remove_note, get_number_of_pages
 #Notebook_variable : title, page_number, notes
 #Note_method : write_content, remove_all
 #Note_variable : content




class Note():
    def __init__(self, content):
        self.content = content

    def write_content(self, content):
        self.content = content ################

    def remove_call(self, content):
        self.content = "" #콘텐트 내용 지우기

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return self.content

#26:40



class NoteBook():
    def __init__(self, title, page_num, notes):
        self.title = title
        self.page_num = page_num
        self.notes = notes

    def add_note(self, page_num):
        pass

    def remove_note(self, page_num):
        pass

    def get_num_of_pages(self):
        pass

