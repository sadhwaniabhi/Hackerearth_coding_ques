
#funtion
def help_chotu(s,l,k):
    for i in range(0,l-1):
        x=set()                   #create the set of list which will have all the unique values so that to check chotu can't visit the same place twice
        curr_sum=k-s[i]
        for j in range(i+1,l):
            if (curr_sum-s[j]) in x:
                return "YES"
            x.add(s[j])
    return "NO"

#inputs 
number=int(input())    #total no of places
Si=input()             #Si value of places
si_array=[]                
for n in Si.split():          #changing the string value entered by user to list so that we can iterate through it
  si_array.append(int(n))

si_length=len(si_array)
k=int(input())        #total threat value of three places
