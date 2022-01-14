import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

IDX_LIST = [0, 2, 4, 8, 12, 14, 18, 22, 26, 30, 34, 36]
IDX_LEN_LIST = [2, 2, 4, 4, 2, 4, 4, 4, 4, 4, 2, 2]

STX_IDX, TYPE_IDX, OUTLET_IDX, INS_IDX, FLAG_IDX, ML_IDX = 0, 2, 4, 8, 12, 14
STX_LEN, TYPE_LEN, OUTLET_LEN, INS_LEN, FLAG_LEN, ML_LEN = 2, 2, 4, 4, 2, 4

CH1VOLT_IDX, CH1AMP_IDX, CH2VOLT_IDX, CH2AMP_IDX, CGTYPE_IDX, CGORD_IDX = 18, 22, 26, 30, 34, 36
CH1VOLT_LEN, CH1AMP_LEN, CH2VOLT_LEN, CH2AMP_LEN, CGTYPE_LEN, CGORD_LEN = 4, 4, 4, 4, 2, 2

with open('D:\\EVC_LOG.txt', "rt", encoding='UTF8') as file:
    strings = file.readlines()
    data = []
    for str_one in strings:
        str_one = str_one.strip().split('[6338(c8)] : ')
        if len(str_one) == 1:
            continue
        str_one = str_one[1].strip()
        data_s = []
        for i in range(len(IDX_LIST)):
            data_s.append(str_one[IDX_LIST[i]:IDX_LIST[i] + IDX_LEN_LIST[i]])
        data.append(data_s)

colums = ['STX', 'TYPE', 'OUTID', 'INS', 'FLAG', 'ML', 'CH1V', 'CH1A', 'CH2V', 'CH2A', 'CGTYPE', 'CGORD']
df = pd.DataFrame(data, columns=['STX', 'TYPE', 'OUTID', 'INS', 'FLAG', 'ML', 'CH1V', 'CH1A', 'CH2V', 'CH2A', 'CGTYPE',
                                 'CGORD'])

df['CH1V'] = df['CH1V'].apply(int, base=16)
df['CH1A'] = df['CH1A'].apply(int, base=16)
df['CH2V'] = df['CH2V'].apply(int, base=16)
df['CH2A'] = df['CH2A'].apply(int, base=16)

print(df['INS'].unique())


condition1 = (df['CH1V'] > 500) & (df['CH2V'] > 200)
print(df[colums][condition1])
#
# condition2 = (df['CH1A'] > 0) & (df['CH2A'] > 0)
# print(df[['CH1A', 'CH2A']][condition2])
#
# plt.scatter(df['CH1V'], df['CH2V'])
# plt.show()
#
# plt.scatter(df['CH1A'], df['CH2A'])
# plt.show()
