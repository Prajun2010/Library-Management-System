''' This module arrange the given list of books
to display on the screen'''

import read # importing read module

def display(database): # declaring display function and passing database parameter
    
    print("\n===========================================================================================")
    print("S.No\tBook Name\t\t\tAuthor\t\t\tQuantity\tPrice")
    print("===========================================================================================")
    
    for index in range(len(database)): # index starts from 0 to length (database-1)
        
        if index==0 or index==1: # for book 1 and 2 in the list database
            
            print("",index+1,end="\t") # for S.N
            print(database[index][0]+"\t\t"+database[index][1]+"\t\t"+"  "+database[index][2]+"\t\t"+"$"+database[index][3])
            
        if index==2: # for book 3 in the list database
            
            print("",index+1,end="\t") # for S.N
            print(database[index][0]+"\t\t\t\t"+database[index][1]+"\t\t"+"  "+database[index][2]+"\t\t"+"$"+database[index][3])
            
        if index==3: # for book 4 in the list database
            
            print("",index+1,end="\t") # for S.N
            print(database[index][0]+"\t\t\t"+database[index][1]+"\t\t"+"  "+database[index][2]+"\t\t"+"$"+database[index][3])
            
        if index==4: # for book 5 in the list database
            
            print("",index+1,end="\t") # for S.N
            print(database[index][0]+"\t\t"+database[index][1]+"\t"+"  "+database[index][2]+"\t\t"+"$"+database[index][3])
            
    print("===========================================================================================")
