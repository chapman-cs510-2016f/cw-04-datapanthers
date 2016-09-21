#!/usr/bin/env python3
def e(n):
    i=2 
    x= []
    while i<n:
        x.append(i)
        i += 1 
        
    #i=1
    #while i<len(x):
    #    if x[i]%2 == 0:
    #        x.remove(x[i])
    #    i += 1
            
    counter = 0
    while counter<len(x):
        count2 = counter+1
        while count2<len(x):
            if x[count2]%x[counter] == 0:
                x.remove(x[count2])
            count2 += 1
        counter += 1

        
          
            
        
    
    
    #print (x)
    return x
        

