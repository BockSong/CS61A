HW_SOURCE_FILE = 'hw04.py'

################
# Linked Lists #
################

# Linked List definition
empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))


def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def isempty(s):
    """Returns True iff s is the empty list."""
    return s is empty


def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

def change(lst, s, t):
    """Returns a link matching lst but with all instances of s (if any)
    replaced by t.

    >>> lst = link(1, link(2, link(3)))
    >>> new = change(lst, 3, 1)
    >>> print_link(new)
    1 2 1
    >>> newer = change(new, 1, 2)
    >>> print_link(newer)
    2 2 2
    >>> newest = change(newer, 5, 1)
    >>> print_link(newest)
    2 2 2
    """
    counter,temp=0,lst
    while rest(temp)!=empty:
        temp=rest(temp)
        counter+=1
    if first(temp)!=s:
        result=link(first(temp))
    else:
        result=link(t)
    while counter>0:
        counter-=1
        temp,counter2=lst,counter
        while counter2>0:
            temp=rest(temp)
            counter2-=1
        if first(temp)==s:
            result=link(t,result)
        else:
            result=link(first(temp),result)
    return result

def reverse_iterative(s):
    """Return a reversed version of a linked list s.

    >>> primes = link(2, link(3, link(5, link(7, empty))))
    >>> reversed_primes = reverse_iterative(primes)
    >>> print_link(reversed_primes)
    7 5 3 2
    """
    result=link(first(s))
    while rest(s)!=empty:
        s=rest(s)
        result=link(first(s),result)
    return result

def reverse_recursive(s):
    """Return a reversed version of a linked list s.

    >>> primes = link(2, link(3, link(5, link(7, empty))))
    >>> reversed_primes = reverse_recursive(primes)
    >>> print_link(reversed_primes)
    7 5 3 2
    """
    temp=s
    while rest(temp)!=empty:
        temp=rest(temp)
    return helper_function(s,temp)

def helper_function(s,newhead):
    if s==newhead:
        return link(first(s))
    else:
        temp=s
        while rest(temp)!=newhead:
            temp=rest(temp)
        return link(first(newhead),helper_function(s,temp))

def insert(lst, item, index):
    """Returns a link matching lst but with the given item inserted at the
    specified index. If the index is greater than the current length, the item
    is appended to the end of the list.

    >>> lst = link(1, link(2, link(3)))
    >>> new = insert(lst, 9001, 1)
    >>> print_link(new)
    1 9001 2 3
    >>> newer = insert(new, 9002, 15)
    >>> print_link(newer)
    1 9001 2 3 9002
    """
    temp,length=lst,0
    while temp!=empty:
        temp=rest(temp)
        length+=1

    counter,temp=0,lst
    while rest(temp)!=empty:
        temp=rest(temp)
        counter+=1
    if index<length:
        result=link(first(temp))
    else:
        result=link(item)
        result=link(first(temp),result)

    while counter>0:
        if counter==index:
            result=link(item,result)
            index+=1
            continue
        counter-=1
        temp,counter2=lst,counter
        while counter2>0:
            temp=rest(temp)
            counter2-=1
        result=link(first(temp),result)
    return result

#########
# Trees #
#########

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(root(t), [copy_tree(b) for b in branches(t)])

def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and
    False otherwise.

    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    if root(t)=='acorn':
        return True
    else:
        total=False
        for x in branches(t):
            total=total or acorn_finder(x)
        return total

def getbone(t):
    if is_leaf(t):
        return tree(0)
    else:
        result=tree(0,[])
    for x in branches(t):
        result.append(getbone(x))
    return result

def same_shape(t1, t2):
    """Return True if t1 is indentical in shape to t2.

    >>> test_tree1 = tree(1, [tree(2), tree(3)])
    >>> test_tree2 = tree(4, [tree(5), tree(6)])
    >>> test_tree3 = tree(1,
    ...                   [tree(2,
    ...                         [tree(3)])])
    >>> test_tree4 = tree(4,
    ...                   [tree(5,
    ...                         [tree(6)])])
    >>> same_shape(test_tree1, test_tree2)
    True
    >>> same_shape(test_tree3, test_tree4)
    True
    >>> same_shape(test_tree2, test_tree4)
    False
    """
    return getbone(t1)==getbone(t2)

def add_branches(tree,subtree):
    tree.insert(len(branches(tree))+1,subtree)
    return tree

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if t1==empty:
        return t2
    if t2==empty:
        return t1
    else:
        if len(branches(t1))!=len(branches(t2)):
            if len(branches(t1))>len(branches(t2)):
                while len(branches(t1))>len(branches(t2)):
                    t2=add_branches(t2,tree(0))
            else:
                while len(branches(t2))>len(branches(t1)):
                    t1=add_branches(t1,tree(0))
        return tree(root(t1)+root(t2),[add_trees(branches(t1)[x1],branches(t2)[x2]) for x1 in range(len(branches(t1))) for x2 in range(len(branches(t2))) if x1==x2])

###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size)

def size(w):
    """Select the size of a weight."""
    return root(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    return not sides(w)

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def total_weight_side(s):
    return total_weight(end(s))

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    if length(sides(m)[0])*total_weight_side(sides(m)[0])!=length(sides(m)[1])*total_weight_side(sides(m)[1]):
        return False
    else:
        result=True
        for x in sides(m):
            if not is_weight(end(x)):
                result=result and balanced(end(x))
        return result
