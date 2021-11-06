"""In case where we need to permute two values there is a simple way to do so"""
a = 5
b = 3
print('a = {} & b = {}'.format(a,b))
a,b = b,a
print('a = {} & b = {}'.format(a,b))
