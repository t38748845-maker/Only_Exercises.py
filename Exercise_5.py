#_Q.1 Performing a simple linear regression to find the m and b values tha minimize loss(sum of squares).
# importing pandas as pd...
import pandas as pd

# importing matplotlib.pyplot as plt...
import matplotlib as plt

# importing LinearRegression from sklearn.linear_model...
from sklearn.linear_model import LinearRegression

# import points...
# https://bit.ly/3C8JzrM
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 4, 6, 8, 10]
}
df = pd.DataFrame(data)

# extract input variables...
X = df.values[:,:-1]
				
# extract output variables...
Y = df.values[:,-1]
				
# fit a line to the points...
fit = LinearRegression().fit(X, Y)

# m = 1.75919315
m = fit.coef_.flatten()

# b = 4.69359655
b = fit.intercept_.flatten()

# prints m...
print("m = {0}.format(m)")

# prints b...
print("b = {0}.format(b)")

# show in chart...
# scatterplot...
plt.plot(X,Y,'o')

# line...
plt.plot(X, m * X + b)

# show...
plt.show()

#_Q.2 Calculate the correlation coefficient and staistical sifnificance at 95% confidence. Is the correlation useful?
# importing pandas as pd...
import pandas as pd

# read data into pandas dataframe...
# https://bit.ly/3C8JzrM
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 4, 6, 8, 10]
}
df = pd.DataFrame(data)
'

# print correlation between variables...
correlation = df.corr(method='pearson')

# prints correlation...
print(correlation)

# test for statistical sifnidicance...
# importing t from scipy.stats...
from scipy.stats import t

# importing sqrt from math...
from math import sqrt

# samplw size...
n = df.shape[0]

# prints n...
print(n)

# define lower cumulative value...
lower_cv = t(n-1).ppf(0.025)

# define upper cumulative value...
upper_cv = t(n-1).ppf(0.975)

# retrieve correlation coefficient.
r = correlations["y"]["x"]

# perform the test...
test_value = r / sqrt((1 - r ** 2) / (n - 2))

# prints test value...
print("TEST VALUE: {}".format(test_value))

# printing critical range...
print("CRITICAL RANGE: {}, {}". format(lower_cv, upper_cv))

# applies for-loop...
# applies if-else conditions...
# applied if statement...
if test_value < lower_cv or test_value > upper_cv:
    
# prints if statement...    
    print("CORRELATION PROVEN, REJECTE HO.\n")

# applied else statement...        
else:
    
# prints else statement...    
    print("CORRELATION NOT PROVEN, FAILED TO REJECT HO.\n")
    
# calculate p-value...
# appplies for-loop...
# applies if-else conditions...
# applied if-statments... 
if test_value > 0:
    
# prints if statement...        
    p_value = 1.0 - t(n-1).cdf(test_value)
    
# applied else statement...        
else:
    
# prints else statement...        
    p_value = t(n-1).cdf(test_value)
    
# apply two-tailed test, so multiply by 2...
p_value = p_value * 2

# prints p_value... 
print("P-VALUE: {}". format(p_value))

#_Q.3 If I predict where x = 50. What is the 95% prediction interval for the predicted value y?
# importing pandas as pd...
import pandas as pd

# importing t from scipy.stats...
from scipy.stats import t

# importing sqrt from math...
from math import sqrt

# load the data...
# https://bit.ly/3C8JzrM
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 4, 6, 8, 10]
}
df = pd.DataFrame(data)
print("df")

# linear regression line...
# value for m...
m = 1.75919315

# value for b...
b = 4.69359655

# calculate prediction interval for x = 50...
x_0 = 50

# formulate for mean...
x_mean = sum(p.x for p in points) / len(points)

# formulate for standard error...
standard_error = sqrt(sum((p.y - (m * p.x + b)) ** 2 for p in points) /
                      (n - 2))

# formulate for margine error...
margin_of_error = t_value * standard_error * \
                  sqrt(1 + (1 / n) + (n * (x_0 - x_mean) ** 2) / \
                       (n * sum(p.x ** 2 for p in points) -
                        sum(p.x for p in points) ** 2))

predicted_y = m * x_0 + b

# Calculate prediction interval
print(predicted_y - margin_of_error, predicted_y + margin_of_error)

#_Q.4 Start your regression over and do a train/test split feel free to experiment with cross-validation and random-fold validation does the linear regression perform well and consistently on the testing data? Why or why not?
# importing pandas as pd...
import pandas as pd

# importing LinearRegression from sklearn.linear_model...
from sklearn.linear_model import LinearRegression

# importing KFold, cross_val_score from sklearn.model_selection
from sklearn.model_selection import KFold, cross_val_score

# import points...
# https://bit.ly/3C8JzrM
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 4, 6, 8, 10]
}
df = pd.DataFrame(data)
print("df")

# extract input variables...
X = df.values[:,:-1]
				
# extract output variables...
Y = df.values[:,-1]
    
# perform simple linear regression...
# for kfold = KFold...
kfold = KFold(n_splits=3, random_state=7, shuffle=True)

# model = LinearRegression...
model = LinearRegression()

# results = cross_val_score
results = cross_val_score(model, X, Y, cv=kfold)

# prints results...
print(results)