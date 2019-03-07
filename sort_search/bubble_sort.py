
def bubble_sort(alist):
    """bubble sort"""
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]

    
if __name__ =='__main__':
    li =[45,3,235,23,56,62,223,34,94,53,23,85,39,29,45,33]
    print(li)
    bubble_sort(li)
    print(li)