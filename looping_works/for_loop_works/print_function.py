
"\n => new line  \t => tab space"

print("smaple",end="\t")

print("test")

#c          c1     c2      c3      c4 
#r3         3,1    3,2      3,3     3,4
#r2         2,1    2,2      2,3     2,4
#r1         1,1    1,2      1,3     1,4


# for r in range(1,4):

#     for c in range(1,5):

#         print(r,c,end="\t")

#     print()


"""
1,1     1,2     1,3     1,4    

2,1     2,2     2,3     2,4    

3,1     3,2     3,3     3,4    

4,1     4,2     4,3     4,4    

"""


"""
1   2   3   4

1   2   3   4

1   2   3   4

"""

# for r in range(1,4):

#     for c in range(1,5):
            
#         print(c,end="\t")    
     
#     print()
"""
#       c1  c2  c3  c4
        O   E   O   E

        O   E   O   E

        O   E   O   E

        O   E   O   E

"""

# for r in range(1,5):

#     for c in range(1,5):

#         if c == 1 or c==3:

#             print("O",end="\t")
#         else:

#             print("E",end="\t")
        
#     print()

"""
     c1   c2  c3
     
 r1   1   0   0
    
    
 r2   0   1   0
 
 r3   0   0   1

"""

for r in range(1,4):

    for c in range(1,4):

        if r==c:

            print(1,end="\t")
        else:
            print(0,end="\t")

    print()

"""
1   1   1   1
1   0   0   1
1   0   0   1
1   1   1   1

"""

"""
1   1   1   1
0   0   0   0
1   1   1   1
0   0   0   0

"""
