n=int(input("Enter number of men: "))
men_pref_list=[]
women_pref_list=[]
list=[]
count=[]

print("Enter preference list of men: ")
for i in range(n):
    p=input()
    men_pref_list.append([int(j) for j in p.split()])

print("Enter preference list of women: ")
for i in range(n):
    p=input()
    women_pref_list.append([int(j) for j in p.split()])

wife=[-1]*n
husband=[-1]*n
list_free_men=[-1]*n
inverse_pref_list_women=[]
for i in range(0,n):
    for j in range(0,n):
        list.append(women_pref_list[i].index(j))
    inverse_pref_list_women.append(list)
    list=[]
#print(inverse_pref_list_women)
m=0
while -1 in list_free_men and -1 in wife:
    m=list_free_men.index(-1)
    for j in range(0,n):
        pref=men_pref_list[m][j]        #pref=highest preference
        if husband[pref]==-1:
            wife[m]=pref
            husband[pref]=m
            list_free_men[m]=1
            break
        elif inverse_pref_list_women[pref][m]<=inverse_pref_list_women[pref][husband[pref]]:
            wife[m]=pref
            temp=husband[pref]
            husband[pref]=m
            list_free_men[m]=1
            list_free_men[temp]=-1
            break
print("Pairs:")
for i in range(0,n):
    print("["+str(i)+","+str(wife[i])+"]",end=" ")

    

