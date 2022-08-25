from math import ceil, log2;
 
def getMid(s, e) :
    return s + (e -s) // 2;

def getSumUtil(st, ss, se, qs, qe, si) :
 
    if (qs <= ss and qe >= se) :
        return st[si];
 
    if (se < qs or ss > qe) :
        return 0;
 
    mid = getMid(ss, se);
     
    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2);
           

def updateValueUtil(st, ss, se, i, diff, si) :
    if (i < ss or i > se) :
        return;
    st[si] = st[si] + diff;
     
    if (se != ss) :
     
        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i,diff, 2 * si + 1);
                        
        updateValueUtil(st, mid + 1, se, i, diff, 2 * si + 2);
                        
def updateValue(arr, st, n, i, new_val) :
 
    if (i < 0 or i > n - 1) :
         
        return;
    
    diff = new_val - arr[i];
 
    # Update the value in array
    arr[i] = new_val;
    # Update the values of nodes in segment tree
    updateValueUtil(st, 0, n - 1, i, diff, 0);
 
# Return sum of elements in range from
# index qs (query start) to qe (query end).
# It mainly uses getSumUtil()
 
# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si) :
 
    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if (ss == se) :
     
        st[si] = arr[ss];
        return arr[ss];
     
    mid = getMid(ss, se);
     
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + constructSTUtil(arr, mid + 1, se, st, si * 2 + 2);
             
     
    return st[si];
 
def constructST(arr, n) :
 
    x = (int)(ceil(log2(n)));
 
    max_size = 2 * (int)(2**x) - 1;
     
    # Allocate memory
    st = [0] * max_size;
 
    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, st, 0);
 
    # Return the constructed segment tree
    return st;
 
# Driver Code

n=int(input())
arr=list(map(int,input().split()))
arr3=arr.copy()
arr2=[1]*n
st = constructST(arr, n);
st2 = constructST(arr2, n);

Q=int(input())
for i in range(Q):
    x= input().split()
    typ=int(x[0])
    if(typ==1):
        y=int(x[1])
        if(arr2[y-1]==1):
            updateValue(arr, st, n, y-1, 0);
            updateValue(arr2, st2, n, y-1, 0);
        else:
            updateValue(arr, st, n, y-1, arr3[y-1]);
            updateValue(arr2, st2, n, y-1, 1);
    else:
        a=int(x[1])
        b=int(x[2])
        total = getSumUtil(st, 0, n - 1, a-1, b-1, 0);
        num=getSumUtil(st2, 0, n - 1, a-1, b-1, 0);
        if(num==0):
            print(-1)
        else:
            print(int(total/num))