''' This module interconnects borrow,read,diplay
and give module,so that users can pass through
each module easily'''

import borrow,read,display,submit # importing modules

def selection(): # defining selection functions
    
    print("\n\t\t\tMain Menu")
    print("\t\t\t=========")
    print("\nPlease choose the given options:")
    print("==================================================")
    print("1. Borrow Books\t\t\t2. return Books\n3. Check library \t\t4. Exit")
    print("==================================================")

    check=True # assigning boolean value in the variable  
    while check==True: # checking variable using while loop
        
        # allowing user to choose the following options by entering the number given on the options
        student_input=input("which options do you want to choose?:")  
        
        if(student_input=="1"): # checking conditon, if input is 1, user can borrow book
            display.display(read.library())# making object of display module and calling read module using display function 
            borrow.borrow(read.library()) # making object for borrow module and calling read module using borrow function
            check=False # assigning opposite boolean value in the varibale, to terminate the loop
            
        elif(student_input=="2"): # checking condition, if input is 2, user can return book 
            display.display(read.library()) #calling read module using display function of display module
            submit.return_back() #calling read module using return_back function of give module
            check=False # assigning opposite boolean value in the varibale, to terminate the loop
            
        elif(student_input=="3"): # checking condition, if input is 3, user can view the books  
            display.display(read.library())
            print("1. Borrow Books\t\t\t2. return Books\n3. Exit")
            print("===========================================================================================")
            stud_input=input("Please choose the given options for further process:")
            
            if stud_input=="1": # if input(1), call borrow module
                borrow.borrow(read.library())
                
            elif stud_input=="2": # if input(2), call submit module 
                submit.return_back()
                
            else:# else, exit from program
                exit
                
            check=False
            
        elif(student_input=="4"): # checking condition, if input is 4, user can exit from the program 
            exit
            check=False
            
        else: # checking condition, if any other input, the while loop runs again 
            print("\nInvalid choice, Please choose again!")
            print("\n")
            check=True

