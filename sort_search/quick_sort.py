def quick_sort(alist,first,last):
    
    low = first
    high = last
    
    if first>=last:
        return
    else:
        mid_value = alist[low]
    
        while low<high:
            while low<high and alist[high]>=mid_value:
                high-=1
            alist[low] = alist[high]
            while low<high and alist[low]<mid_value:
                low+=1
            alist[high] = alist[low]
        alist[low] = mid_value
        quick_sort(alist, 0, low)
        quick_sort(alist, low+1, last)
        
if __name__ =='__main__':
    li =[45,3,235,23,56,62,223,34,94,53,23,85,39,29,45,33]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)  