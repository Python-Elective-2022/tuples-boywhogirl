input = ('I', 'am', 'a', 'test', 'tuple')


#The x in function  is a variable  that represent what input you want to skip tuples, 
# we going to return the input tuple is skipped starting with the first tuple.
def skip_tuples(x):
    return x[::2]

print(skip_tuples(input))


        


