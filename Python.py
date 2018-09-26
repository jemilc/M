17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 ** 2  # 5 squared
'doesn\'t'  # use \' to escape the single quote...
>"doesn't"
"\"Yes,\" they said."
>'"Yes," they said.'
word = 'Python'
word[0]  # character in position 0
>'P'
word[2:5]  # characters from position 2 (included) to 5 (excluded)
>'tho'
'J' + word[1:]
>'Jython'

List
----
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
>[['a', 'b', 'c'], [1, 2, 3]]
x[0]
>['a', 'b', 'c']
x[0][1]
>'b'

WHILE
-----
a, b = 0, 1
while a < 1000:
     print(a, end=',')
     a, b = b, a+b
IF
--

x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
     x = 0
     print('Negative changed to zero')
 elif x == 0:
     print('Zero')
 elif x == 1:
     print('Single')
 else:
     print('More')
> More

words = ['cat', 'window', 'defenestrate']
for w in words:
     print(w, len(w))
> cat 3
> window 6
> defenestrate 12

FOR
---
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
     print(i, a[i])
0 Mary
1 had
2 a
3 little
4 lamb

LAMBDA
------
def make_incrementor(n):
     return lambda x: x + n

f = make_incrementor(42)
f(0)
> 42
f(1)
> 43

Code
-----
# run everything when calling script from CLI
if __name__ == "__main__":
	main()
np.mean(np.abs(pred-obs))
np.arange(0.01,0.99,0.01)
apply(lambda x: 1 if x else 0))

Modules
---
### Panda ### 
Series
-------
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
apply(func[, convert_dtype, args])	Invoke function on values of Series.
Ex: pandas.Series(pred > cutoff).apply(lambda x: 1 if x else 0)

### SKLearn ###
Metrics
--------
sklearn.metrics.f1_score(y_true, y_pred, labels=None, pos_label=1, average=’binary’, sample_weight=None)
F1 = 2 * (precision * recall) / (precision + recall)
Ex:
>>> from sklearn.metrics import f1_score
>>> y_true = [0, 1, 2, 0, 1, 2]
>>> y_pred = [0, 2, 1, 0, 0, 1]
>>> f1_score(y_true, y_pred, average='macro')  
0.26...
>>> f1_score(y_true, y_pred, average='micro')  
0.33...
>>> f1_score(y_true, y_pred, average='weighted')  
0.26...
>>> f1_score(y_true, y_pred, average=None)
array([0.8, 0. , 0. ])

Ex: f1_score(obs,pd.Series(pred > cutoff).apply(lambda x: 1 if x else 0)) #puede ser reemplazado por 1??









