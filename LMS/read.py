'''This module consist of library function which has been created
to convert strings, content in the text file(books.txt) to
integers and to store in 2D list(database)'''

def library(): # declaring library functions
    database=[] # creating list to store data

    file=open("books.txt","r")# It opens the file books.txt and read the contents
    for each in file:
         # splitting and storing each item on the basis of (,) in the list
         # also replace(\n),to prevent it from diplaying on the screen
        database.append(each.replace("\n","").split(","))  
    file.close()
    return database # returning database


    
    
