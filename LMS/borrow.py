''' This module consist the function
for borrowing the books from the database
and creating file for borrow'''

import datetime,choose # importing datetime module from python library class
def borrow(database): # defining borrow function in borrow module, calling database list
    
    invo_list=[] # new list to store the borrowed item
    
    total=0 # delcaring variable for amount addition of the books
    
    full_name=input("\nPlease enter your full name:") # username full name entry section

    ask_user="y" or "Y" # initializing variable with character  
    while ask_user=="y" or ask_user=="Y": # chekcing input for loop process for borrowing more
        
        check=True #declaring and assigning boolean value to the variable
        while check==True: # chekcing input for loop process for valid serial number 
            
            book_serialNo=input("\nEnter serial number:")
            
            # can pass through if only the assigned value are matched
            if book_serialNo=="1" or book_serialNo=="2" or book_serialNo=="3" or book_serialNo=="4" or book_serialNo=="5":
                
                for i in range(len(database)):
                    if int(book_serialNo)-1==i:
                        file=open(full_name+".txt","w") #overwriting section for borrwed books 
                        file.write("\nThank you "+full_name+"!, for borrowing the books\n\nThe books you borrowed are listed below:\n")

                        if int(database[i][2])>0: #if quantity of books are available
                            database[i][2]=int(database[i][2])-1 # decreasing if borrowed and storing latest quantity of book 
                            
                        else: # if qunatity of books are out of stocks
                            print("Sorry! We are out of stock for this item")

                        check=False # assigning boolean value to the variable
                        
                        invo_list.append(database[i][0]+","+database[i][1]+","+"$"+database[i][3]+"\n") # storing borrowed item in the list
            
                        total=float(total)+float(database[i][3]) # amount addition section
                        return_date=(datetime.datetime.now().date()+datetime.timedelta(days=10))# setting return date for 10 days
                        
                        # This section writes borrwed list in the text 
                        for i in range(len(invo_list)):
                            select=i+1
                            file.write(str(select))
                            file.write(" ")
                            file.write(str(invo_list[i]))
                            
                        file.write("\n-------------------------------------------")
                        file.write("\nTotal price: $"+str(total)) # total amount of books here
                        file.write("\nBorrowed date:"+str(datetime.datetime.now().date())) # borrowed date here
                        file.write("\nReturning Date:"+str(return_date)) # assingned returned date here
                        file.close()

                        # This section overwrites the borrowed item in the given text path
                        returntime=open(""+full_name+"_return.txt",'w')
                        for i in range(len(invo_list)):
                            returntime.write(str(invo_list[i])) # writing list stored in the list 
                        returntime.write(str(return_date)) # return date over here 
                        returntime.close()
                        
            else: # if invalid number input
                print("\nInvalid serial number, Please enter again !")
                check=True
                
        ask_user=input("Do you want to borrow next book ?(Y/N):") # asking for character to continue the loop
#all loops ends here
                
# display section
# diplays borrowed item saved in the specific text
    file=open(full_name+".txt","r")
    print("\n=======================================================")
    for each in file:
        print(each)
    print("=========================================================")
    file.close()
        
# overwrite section
# This section consist of file overwrite where previous data in text file are overwrite by new data
    file=open("books.txt","w")
    for i in range(len(database)):
        final_list=database[i][0]+","+database[i][1]+","+(str(database[i][2]))+","+database[i][3]+"\n"
        file.write(final_list)
    file.close()

# calling selection function from choose module
    menu_call=input("Do you want to return back to Main Menu?(Y/N):")
    try:
        if menu_call=="y" or menu_call=="Y":
                        choose.selection()
    except:
                    exit
                
            

    
    
        
        

        



        

    


    
            
            

    
            
            

    
    
