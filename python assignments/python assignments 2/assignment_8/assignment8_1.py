class BookStore():

    NoofBooks = 0


    def __init__(self,A,B):
        self.Name= A
        self.Author=B
        BookStore.NoofBooks +=1 

    
    def Display(self):
        print("name of the book : ", self.Name , "by ", self.Author, " number of books : ", BookStore.NoofBooks)
        


Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()   
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()   
