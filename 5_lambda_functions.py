print((lambda x, y: x + y)(5, 7))
# or
sub = lambda x, y: x - y
print(sub(5, 7))


# map and lambda functions
def double(x):
    return x * 2


seq = [0, 2, 4, 6]
double_seq = [double(x) for x in seq]
# same
double_seq = map(double, seq)

# using lambda
double_seq = map(lambda x: x * 2, seq)
print(list(double_seq))
