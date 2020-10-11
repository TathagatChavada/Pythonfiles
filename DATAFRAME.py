import pandas as pd   # For converting your data into tabular form

# Create any kind of dictionary you want
Table = {"BIN": [0000,1,10,11,100,101,110,111,1000,1001,1010,1011,1100,1101,1110,1111],
         "HEX": [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'],
         "OCT": [0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17],
         "DEC": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}

print('\n')

X = pd.DataFrame(Table)
print(X)



