import pandas as pd

test=[[1,2,3],[4,5,6]]

df = pd.Series(test)
df = pd.DataFrame(test,columns=['source','target','pollution'],index=None)
df.to_csv('./test.csv',index=None)