
def select_sort(alist):
    """select sort"""
    for i in range(len(alist)-1):
        max_index = 0
        for j in range(1,len(alist)-i):
            if alist[max_index]<alist[j]:
                max_index = j
        
        alist[len(alist)-1-i],alist[max_index]=alist[max_index],alist[len(alist)-1-i]

    
if __name__ =='__main__':
    li =[45,3,235,23,56,62,223,34,94,53,23,85,39,29,45,33]
    print(li)
    select_sort(li)
    print(li)