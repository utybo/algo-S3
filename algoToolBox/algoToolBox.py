
# coding: utf-8

# # Algo Toolbox and "*Pythoneries*"
# ## Lists

# ### **<font color="blue">Exercise: Split List</font>**
# Write a function that splits a list of length *n*, with *n* odd, into 3 parts: 
# - the elements of the first half of the list (without the middle one)
# - the middle element
# - the elements of the second half of the list (without the middle one)
# 

# In[ ]:

def splitlist(L):
    #FIXME
    pass


# #### Pythonery
# This can be simplified with *Python list slices*:
# - `L[a:b]` is the sub list of `L` with elements from positions `a` to `b` (`b` excluded)
# - `L[:a]` is the list `L[0:a]`
# - `L[a:]` is the list `L[b:len(n)]`
# - `L[-1]` is `L[len(L)]`

# In[ ]:

def splitlist(L):
    #FIXME
    pass

# In[ ]:

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
splitlist(L)


# ### **<font color="blue">Exercise: Binary Search</font>**
# Write two functions to search an element in a sorted (in increasing order) list:
# - `binarysearch(L, x, left, right)` returns the position where `x` is or might be in `L[left, right[`, with `L` sorted in increasing order.
# 

# In[ ]:

def binarysearch(L, x, left, right):
    """Binary Search
    
    Args:
        L: List to search in
        x: Value to search
        left, right: Search intervalle in L [left, right[
        
    Returns:
        The position where x is or might be
    """

    #FIXME
    pass

# In[ ]:

L = [-3, 0, 5, 8, 13, 24, 32, 37, 42]


# In[ ]:

binarysearch(L, 0, 0, len(L))


# - `listSearch(L, x)` returns `-1` if `x` in not in the list `L`, its position otherwise

# In[ ]:

def listsearch(L, x):
    #FIXME
    pass

# #### Pythonery
# Use *Python "ternary" operator*:
# `[on_true] if [expression] else [on_false]`

# In[ ]:

def listsearch2(x, L):
    #FIXME
    pass

# ### **<font color="blue">Exercise: Build List &rarr; Build Matrix</font>**
# Write the function `buildlist(nb, val=None, alea=None)` that builds a new list of length `nb`:
# - `buildlist(nb)` returns  `[None, None, ...]`
# - `buildlist(nb, val)` returns `[val, val, ...]`
# - `buildlist(nb, alea = (a, b))` returns a list of `nb` random values in `[a, b[`

# Note: `if a:` is `False` when `a` is `0, None, [], "" ...`

# In[ ]:

# Reminder on imports, random and seed
import random
help(random.randint)


# In[ ]:

help(random.seed)
random.seed()    # do it once only!


# In[ ]:

def buildlist(nb, val=None, alea=None):
    #FIXME
    pass

# #### Pythonery
# *Python gives a short way to build list*: `[val] * nb`

# In[ ]:

def buildlist(nb, val=None, alea=None):
    #FIXME
    pass

# Test the "short" version (`[val] * n`) with random numbers...

# In[ ]:

[random.randint(0, 10)] * 5


# #### Pythonery: "list comprehension"
# Test the following, then use it to write again `buildlist`

# In[ ]:

[i for i in range(10)]


# In[ ]:

def buildList(nb, val=None, alea=None):
    #FIXME
    pass

# In[ ]:

buildlist(5), buildList(5, 0), buildList(5, alea=(0,10))


# #### <font color="red">WARNING:</font>
# when you want to build a list of lists

# In[ ]:

L = buildList(9, [])


# In[ ]:

L


# In[ ]:

L[0].append(1)


# In[ ]:

L


# Write again `buildlist` to avoid the problem

# In[ ]:

def buildlist(nb, val = None, alea = None):
    #FIXME
    pass

# Use `buildlist` to build a (5*5) matrix filled with `None`, then change a value

# In[ ]:

M = buildlist(4, buildlist(5, None))


# In[ ]:

M


# In[ ]:

M[0][0] = 5


# In[ ]:

M


# Write a function `buildmatrix(line, col, val=None)` that builds a `(line*col)` matrix filled with `val`.

# In[ ]:

def buildmatrix(line, col, val = None):
     #FIXME
    pass

# In[ ]:


M = buildmatrix(4, 5)
M[0][0] = 3
M

