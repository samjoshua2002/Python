'''import pandas as pd
s1=pd.Series([1,2,3],index=['a','b','c'])
print(s1)




import pandas as pd
s1=pd.Series([1,2,3,3,4])
s2=pd.Series([4,7,6,4,3])
print(s1+s2)'''

'''

import pandas as pd
s1=pd.DataFrame({"Name" : ['Bob' , 'Sam' , 'Anne'] , "marks" :[12,34,54]})
print(s1)

output:

   Name  marks
0   Bob     12
1   Sam     34
2  Anne     54




'''

'''
import pandas as pd
read=pd.read_csv("F:\Github\Python\excel.csv")
print(read.describe())


output:

     Sepal.Length  Sepal.Width  Petal.Length  Petal.Width    Species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
3             4.6          3.1           1.5          0.2     setosa
4             5.0          3.6           1.4          0.2     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica
'''


'''
import pandas as pd
read=pd.read_csv("F:\Github\Python\excel.csv")
a=read.iloc[0:3,0:2]
print(a)


output:
   Sepal.Length  Sepal.Width
0           5.1          3.5
1           4.9          3.0
3           4.7          3.2

''' 
