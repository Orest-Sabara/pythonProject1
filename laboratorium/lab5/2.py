sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

print(sample_dict.keys())
print(sample_dict.items())

for k in sample_dict.keys():
    print(f'{k:<7} = {sample_dict[k]:>8}')

for k, v in sample_dict.items():
    print(f'{k:<7} = {v:>8}')