## Math Library for plotting etc - http://matplotlib.org/gallery.html
## Python for Statistical use - http://pandas.pydata.org/talks.html
## Book on Python and Examples - http://greenteapress.com/wp/think-python/

## Creates a 9x9 matrix
table= [ [ 0 for i in range(9) ] for j in range(9) ]
#for row in table:
#     print row

with open("sudoku9927.txt","r") as txt:
     for line in txt:
#         print line
         #for numbers_int in list(line.split('0')):
         #print numbers_int
         for i in range(9):
             for j in range(9):
                 try:
                     table[i][j]=int(line[i*9+j])
                 except ValueError:
                     pass
for row in table:
     print row
print("")

#for i in range(9):
#    for j in range(9):
#        table[i][j] = table[i][j]*2
#for row in table:
#     print row
