list = ['101_1', '102_1', '102_2', '103_1']
list = [x[:-2] if x.endswith('_1') else x for x in list]
print(list)
