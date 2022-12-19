def sum_of_values(dict2):
    result = 0
    for value in dict2.values():
        result += value
    return result
dict1 = {'data1':10, 'data2':-4, 'data3':2}
r = sum_of_values(dict1)
print(r)
