#python script to find permutation of 1,2,3 without using permutation function
#this code is for uses recursive funtion to calculate 1,2,3
#define function for permutation on 1 
def permutation(s):  
    if len(s) == 1:
        print(s)
        return [s]
    
    perm_list = [] # create empty list
    for a in s:
        remaining_elements = [x for x in s if x != a]
        print(remaining_elements)
        z = permutation(remaining_elements)
        print(z)
        for t in z:
            perm_list.append([a] + t)
            print(perm_list)
        
    return perm_list

s = [1,2,3];
p = permutation(s);
print(p)
        
        
        
        
        
    