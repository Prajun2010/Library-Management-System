''' This module consist the return function
for returning the books from the database
and creating file for return'''

from datetime import datetime # importing datetime function from datetime module
import choose # importing choose module

def return_back():  # defining function for submitting book

    global name # global variable declaration
    global fine
    
    # empty list 
    listing=[]  # storing borrowed books
    temp=[] #storing books name 
    store=[] # storing each items from the books.txt
    
    file=open("books.txt","r") # opening and reading contents content in the file 
    for each in file: 
        store.append(each.replace("\n","").split(","))
    file.close()

# display section
# This section consist of list borrowed by specific user

    borrower=True # declaring and assigning boolean value in variable 
    while borrower==True: # checking boolean variable for loop process
        
        name=input("Enter the name by which you borrowed the book: ")
        
        try: # run process if error doesn't occur
            file = open(name+"_return.txt", "r") # reading file 
            for each in file:
                listing.append(each.replace("\n", "").split(","))
            print("\n========================================================")
            print("Following books are borrowed by: "+name+"\n")
            
            for i in range(len(listing)):
                
                if listing[i]==listing[-1]: # breaks the process, if value in index(-1) match index(i)
                    break
                
                print(str(i + 1)+","+listing[i][0]+","+ listing[i][1]+"\n")
            print("========================================================")
            file.close()
            
            borrower=False # assigning boolean value in the variable
            
        except: # if error occurs, run this. 
            print("\nBorrower with name "+name+" not found")
            borrower=True    

# books return loop section

    returnbook=True # declaring and assigning boolean value in the variable
    
    while returnbook==True:# checking boolean value for loop process
        number=input("Enter the serial number of the book you want to return:")
        num_int=int(number) # converting str into int
        book_name=listing[num_int-1][0] # decreaing input number by 1
        
        # for storing name of the books 
        for i in range(len(store)): 
            if book_name.upper()==store[i][0].upper():
                store[i][2]=int(store[i][2])+1
                temp.append(book_name)
                break
            
        return_more=input("\nDo you want to return more?(Y/N):")
        if return_more=="Y" or return_more=="y":
            returnbook=True
        else:
            returnbook=False

# date calculation section here
    return_date=datetime.strptime(listing[-1][0],'%Y-%m-%d') # strptime(change string date to datetime in the given format)
    date_today=datetime.now() # todays date 
    calc=return_date-date_today # decreasing returned date by today date 
    calc=int(calc.days)

    print("=======================================================")

    fine=0 # declaring and initializing fine amount
    
    if calc<0: # if late submitted
        print("\nYou have submitted late.So you will be fined!")
        fine=3*0.5
        print("Fined amount= $",fine)
        
    else: # if submitted on time 
        print("\nThank you for returning the books on time!")
        print("Fined amount= $",fine)
    print("=======================================================")

# overwriting section
# This section overwrites the books list in the books.txt whenever returning the books;
    file=open("books.txt","w")
    for i in range(len(store)):
        final_list=store[i][0]+","+store[i][1]+","+(str(store[i][2]))+","+store[i][3]+"\n"
        file.write(final_list)
    file.close()


# adding returned book list with fine amount in the specific text
    file=open(name+".txt","a")
    # (write) for writing in the text
    file.write("\n=======================================================================")
    file.write("\n\nThank you "+name+"!, for returning the book\n\nThe books are returned:\n\n")
    for i in range(len(temp)):
        sn=i+1 
        file.write(str(sn))
        file.write(" ")
        file.write(str(temp[i])+"\n") # for writing books list stored in temp list
        
    file.write("\nreturned date:"+str(datetime.now().date())) # returned date over here for text
    file.write("\nFined amounnt= $"+str(fine)) # fined amount over here for text
    file.write("\n=======================================================================")
    file.close()

    print("\nThank you "+name+"!, for returning the books")
             

# calling selection function from choose module 
    menu_call=input("Do you want to return back to Main Menu?(Y/N):")
    try:
        if menu_call=="y" or menu_call=="Y":
            choose.selection()
    except:
                    exit


   
    
                
    
        
        
        


