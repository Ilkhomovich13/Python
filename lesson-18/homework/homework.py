import pandas as pd

# 1. 
df = pd.read_csv('lesson-18/tackoverflow_qa.csv')

# 2. 
df['creationdate'] = pd.to_datetime(df['creationdate'])

# 3. 
print('Savollar (2014-yilgacha):')
print(df[df['creationdate'].dt.year < 2014])

# 4. 
print('\nBallari 50 dan katta savollar:')
print(df[df['score'] > 50])

# 5. 
print("\nBallari 50 va 100 oralig'idagi savollar:")
print(df[(df['score'] >= 50) & (df['score'] <= 100)])

# 6. 
print('\nScott Boston javob bergan savollar:')
print(df[df['ans_name'] == 'Scott Boston'])

# 7. 
users = ['Scott Boston', 'Mike Pennington', 'unutbu', 'jezrael', 'DSM']
print('\nTop 5 foydalanuvchilar javob bergan savollar:')
print(df[df['ans_name'].isin(users)])



#####################################################################################


import pandas as pd


titanic = pd.read_csv('lesson-18/titanic.csv')

# 1.
female_class1_20_30 = titanic[
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1) &
    (titanic['Age'] >= 20) &
    (titanic['Age'] <= 30)
]
print("Class1 da, yoshi 20-30 orasidagi ayollar:")
print(female_class1_20_30)

# 2.
fare_above_100 = titanic[titanic['Fare'] > 100]
print("\nChipta narxi $100 dan katta bo'lgan yo'lovchilar:")
print(fare_above_100)

# 3.
survived_alone = titanic[
    (titanic['Survived'] == 1) &
    (titanic['SibSp'] == 0) &
    (titanic['Parch'] == 0)
]
print("\nYolg'iz omon qolgan yo'lovchilar:")
print(survived_alone)

# 4.
embarked_c_above_50 = titanic[
    (titanic['Embarked'] == 'C') &
    (titanic['Fare'] > 50)
]
print("\n'C' portidan chiqqan va $50 dan ortiq to'lov qilganlar:")
print(embarked_c_above_50)

# 5.
with_family = titanic[
    (titanic['SibSp'] > 0) &
    (titanic['Parch'] > 0)
]
print("\nHam SibSp, ham Parch mavjud bo'lgan yo'lovchilar:")
print(with_family)

# 6. 
under15_didnt_survive = titanic[
    (titanic['Age'] <= 15) &
    (titanic['Survived'] == 0)
]
print("\n15 yoshdan kichik bo'lgan va omon qolmagan yo'lovchilar:")
print(under15_didnt_survive)
