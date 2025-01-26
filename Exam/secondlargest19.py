
def second_largest_list(list):
    sortedlist=[]
    for i in range(len(list)-1):
        if list[i]<list[i+1]:
            sortedlist.append(list[i])
        elif list[i]>list[i+1]:
            sortedlist.append(list[i+1])
        else:
            continue
    return sortedlist[-2]

def main():
    list=[1,2,3,4,5,6,7,25,52,8,9,10]
    sorted_list=sorted(list)
    print("Second largest number is:",second_largest_list(sorted_list))
    
main()