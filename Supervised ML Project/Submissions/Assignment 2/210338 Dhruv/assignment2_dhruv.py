import numpy as np
import pandas as pd

# Q1
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

df1 = pd.DataFrame(exam_data)

selected_rows = df1[(df1['attempts'] < 2) & (df1['score'] > 15)]
print("Selected Rows (Q1):")
print(selected_rows)
print()

# Q2a
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

grouped_data = student_data.groupby('school_code')
for group_name, group_data in grouped_data:
    print("Group:", group_name)
    print(group_data)
print()

# Q2b
group_name = 's002'
specific_group = grouped_data.get_group(group_name)
print("Specific Group (Q2b):", group_name)
print(specific_group)
print()

# Q2c
grouped_statistics = grouped_data['age', 'height', 'weight'].agg(['mean', 'std'])
print("Grouped Statistics (Q2c):")
print(grouped_statistics)
print()

# Q3
df3 = pd.DataFrame({
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, "#", 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, "?", 12.43, 2480.4, 250.45, 3045.6],
    'ord_date': ['?', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10',
                 '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, "#", 3002, 3001, 3001],
    'salesman_id': [5002, 5003, "?", 5001, np.nan, 5002, 5001, "?", 5003, 5002, 5003, "#"]
})

df3.replace('?', np.nan, inplace=True)
df3.replace('#', np.nan, inplace=True)
df3.fillna(method='ffill', inplace=True)

print("Modified DataFrame (Q3):")
print(df3)
print()
