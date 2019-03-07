
def insert_sort(alist):
    """insert sort"""
    for i in range(1,len(alist)):
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i-1],alist[i]=alist[i],alist[i-1]
            i-=1
if __name__ =='__main__':
    li =[45,3,235,23,56,62,223,34,94,53,23,85,39,29,45,33]
    print(li)
    insert_sort(li)
    print(li)