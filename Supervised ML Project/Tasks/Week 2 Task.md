 # Pandas Assignment                                               
#### Q1.) Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.

#### DataFrame:<br>
Sample Python dictionary data and list labels:<br>
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],<br>
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],<br>
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],<br>
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}<br>
        
 #### Initial Dataframe looks like:
<pre>
   school class      name        date_Of_Birth   age  height  weight  address
0   s001     V  Alberto Franco     15/05/2002   12    173      35  street1
1   s002     V    Gino Mcneill     17/05/2002   12    192      32  street2
2   s003    VI     Ryan Parkes     16/02/1999   13    186      33  street3
3   s001    VI    Eesha Hinton     25/09/1998   13    167      30  street1
4   s002     V    Gino Mcneill     11/05/2002   14    151      31  street2
5   s004    VI    David Parkes     15/09/1997   12    159      32  street4
</pre>

#### Q2.) a. Write a Pandas program to split the following given dataframe into groups based on school code <br>
#### b. call a specific group with the name of the group.<br>
#### c. find mean and standard deviation of age,height and wieght of all groups formed<br>
#### Dataframe:<br>
student_data = pd.DataFrame({<br>
    'school_code': ['s001','s002','s003','s001','s002','s004'],<br>
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],<br>
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],<br>
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],<br>
    'age': [12, 12, 13, 13, 14, 12],<br>
    'height': [173, 192, 186, 167, 151, 159],<br>
    'weight': [35, 32, 33, 30, 31, 32],<br>
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},<br>
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])<br>
    
#### Initial Dataframe looks like:
<pre>
   school class      name        date_Of_Birth   age  height  weight  address
S1   s001     V  Alberto Franco     15/05/2002   12    173      35  street1
S2   s002     V    Gino Mcneill     17/05/2002   12    192      32  street2
S3   s003    VI     Ryan Parkes     16/02/1999   13    186      33  street3
S$   s001    VI    Eesha Hinton     25/09/1998   13    167      30  street1
S5   s002     V    Gino Mcneill     11/05/2002   14    151      31  street2
S6  s004    VI    David Parkes     15/09/1997   12    159      32  street4
</pre>

#### Q3.) Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.<br>
###### Example: Missing values-> ?, #  <br>
#### Replace those values with NaN and then fill NaN value with the valid value just above it, <br>
#### if just above valid value does not exist fill it with just below valid value<br>
#### Dataframe:
 df = pd.DataFrame({<br>
'ord_no':[70001,np.nan,70002,70004,np.nan,70005,"#",70010,70003,70012,np.nan,70013],<br>
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,"?",12.43,2480.4,250.45, 3045.6],<br>
'ord_date': ['?','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],<br>
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,"#",3002,3001,3001],<br>
'salesman_id':[5002,5003,"?",5001,np.nan,5002,5001,"?",5003,5002,5003,"#"]}) <br>

#### Initial Dataframe looks like :<br>
 <pre>
  ord_no    purch_amt     ord_date   customer_id  salesman_id   <br> 
0   70001     150.5           ?          3002        5002 <br>
1     NaN    270.65     2012-09-10       3001        5003  <br>
2   70002     65.26         NaN          3001           ?  <br>
3   70004     110.5    2012-08-17        3003        5001  <br>
4     NaN     948.5    2012-09-10        3002         NaN  <br>
5   70005    2400.6    2012-07-27        3001        5002  <br>
6      #      5760     2012-09-10        3001        5001  <br>
7   70010         #    2012-10-10        3004           ?  <br>
8   70003     12.43    2012-10-10          #        5003<br>
9   70012    2480.4    2012-06-27        3002        5002<br>
10    NaN    250.45    2012-08-17        3001        5003<br>
11  70013    3045.6    2012-04-25        3001          #<br> </pre>
