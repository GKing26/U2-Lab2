#Griffin King
#U2 Lab 1
# Making a multiplication table with one line



# ONE LINE - NO MORE, NO LESS
table = [(a+1)*(b+1) for a in range(10) for b in range(10)]




########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()
    
    print(num, end="\t")
print()
#################################