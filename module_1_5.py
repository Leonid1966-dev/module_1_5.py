immutable_var = 1, 2, 3, 'a', 'b', 'c'
print(immutable_var)
immutable_var = ([ 1, 2, 3 ], [ 'a', 'b', 'c' ])
print(immutable_var)
immutable_var[0][1] = 5
immutable_var[1][2] = 'gif'
print(immutable_var)




