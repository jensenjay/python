def shell_sort(alist):
    gap = len(alist)
    while gap>=1:         
        gap = gap//2
        
        for i in range(1,gap):
            
            while i>0:
                if alist[gap]<alist[i-gap]:
                    alist[i-gap],alist[i]=alist[i],alist[i-gap]
                i-=gap
            
if __name__ =='__main__':
    li =[45,3,235,23,56,62,223,34,94,53,23,85,39,29,45,33]
    print(li)
    shell_sort(li)
    print(li)  