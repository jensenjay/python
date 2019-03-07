from pandas.tests.frame.test_join import left

def guibin_sort(alist):
    """guibin sort"""
    len_ = len(alist)
    bin_ = len_//2
    if bin_<1:
        return alist
    else:
        left_bin = guibin_sort(alist[:bin_])
        right_bin = guibin_sort(alist[bin_:])
        
        left = 0
        right = 0
        
        li = []
        
        while left<len(left_bin) and right<len(right_bin):
            if left_bin[left]<=right_bin[right]:
                li.append(left_bin[left])
                left+=1
            else:
                li.append(right_bin[right])
                right+=1
        li+=left_bin[left:]
        li+=right_bin[right:]
        
        return li
        
if __name__ =='__main__':
    li =[45,3,235,23,56,62,223,34,94,53,23,85,39,29,45,33]
    print(li)
    li_sorted = guibin_sort(li)
    print(li_sorted)