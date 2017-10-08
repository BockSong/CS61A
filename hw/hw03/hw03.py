HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n<=3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    g1num,g2num,g3num,temp1,temp2=1,2,3,0,0
    step,i=n-3,0
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        while i<step:
            temp1=g1num
            temp2=g2num
            g1num=g2num
            g2num=g3num
            g3num=g3num+2*temp2+3*temp1
            i+=1
        return g3num

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    while k!=0:
        if k%10==7:
            return True
        k=k//10
    return False

def count_times(n):
    i,times=1,0
    while i<=n:
        if i%7==0 or has_seven(i):
            times+=1
        i+=1
    return times

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    if n==1:
        return 1
    if count_times(n-1)%2==0:
        return pingpong(n-1)+1
    else:
        return pingpong(n-1)-1

def count_partitions(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        return count_partitions(n-m,m)+count_partitions(n,m//2)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    if amount==0:
        return 1
    if amount<0:
        return 0
    i=1
    while i*2<=amount:
        i=i*2
    return count_partitions(amount-i,i)+count_partitions(amount,i//2)

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n==1:
        print_move(start,end)
    else:
        if start+end==3:
            move_stack(n-1,start,3)
            print_move(start,end)
            move_stack(n-1,3,3-start)
        elif start+end==4:
            move_stack(n-1,start,2)
            print_move(start,end)
            move_stack(n-1,2,4-start)
        else:
            move_stack(n-1,start,1)
            print_move(start,end)
            move_stack(n-1,1,5-start)

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    newlist=[]
    for element in lst:
        if type(element)!=list:
            newlist.append(element)
        else:
            templist=flatten(element)
            for obj in templist:
                newlist.append(obj)
    return newlist

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    lst=flatten([lst1,lst2])
    for i in range(0,len(lst)):
        minN=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[minN]:
                minN=j
        if minN!=i:
            temp=lst[i]
            lst[i]=lst[minN]
            lst[minN]=temp
    return lst


def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    if len(seq)<=1:
        return seq
    elif len(seq)%2==0:
        lst1=seq[:len(seq)//2]
        lst2=seq[len(seq)-len(seq)//2:]
    else:
        lst1=seq[:len(seq)//2+1]
        lst2=seq[len(seq)-len(seq)//2:]
    return merge(mergesort(lst1),mergesort(lst2))

