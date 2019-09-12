import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv ('https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/ff414a1bcfcba32481e4d4e8db578e55872a2ca1/titanic.csv', sep = '\t')
print(df.info())
print(df.info)
print(df.columns)

print(df[['Age', 'Parch']].describe())
print(df[df['Age']>0] [['Age', 'Parch']].describe())


df['Died'] = df['Survived'] -1
df['AgeMux'] = df['Age'].apply(lambda x: x*2)
print(df[['AgeMux']])

df['AgeMux'].plot('hist')
# plt.show()

# df.to_json('aaa.json')


print(df.dropna().info)
# df = df.fillna(value=df.mean)
print(df.count())

print(df['Embarked'].unique())
print(df['Survived'].unique())
