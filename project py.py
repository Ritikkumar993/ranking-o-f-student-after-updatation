def dictionaray(names,marks):
        d={}
        #taking empty dictionary
        for i in range(len(names)):
            d[names[i]]=marks[i]
        #assining the dicst element
        return list(d.items())

def rank(s):
    for j in range(len(s)-1):
        for i in range(len(s)-1):
            if s[i][1]<s[i+1][1]:

                s[i],s[i+1]=s[i+1],s[i]   
            # else:
            #     s[i],s[i+1]=s[i],s[i+1]
    return s
# def list1(a,s):
#     for i in range(1,len(s)+1):
#         print(a,"Rank: ",i,"  name:",s[i-1][0],"  marks: ",s[i-1][1])

names=["Ronaldo","Rohit","Preeti","Anuska"]
#we can also take names as input from the user
#names=list (map(str,input("Enter all the names with space in it: ").split()))
marks=[12,34,4,50]
#marks=list(map(int,input("Enter all marks respectively with space: ").split()))
s=dictionaray(names,marks)
q=rank(s)
# list1("Previous Rank:",q)

updates=[45,34,301,24]
#updates=list(map(int,input("Enter all updated marks respectively with space: ").split()))
s=dictionaray(names,updates)
p=(rank(s))
# list1=("Current Rank:",p)
for i in range(len(q)):
    if p[0][0] == q[i][0]:
        print("Student who got maximum marks is",p[0][0],"marks:",p[0][1],"jump:",i) 
        