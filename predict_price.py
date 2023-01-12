import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as tts

data = pandas.read_csv('iphone_price.csv')
x = [data['version']]
y = [data['price']]
xtrain, xtest, ytrain, ytest = tts(x,y)

# print(x,y)
print(xtrain)
model = LinearRegression()
model.fit(xtrain, ytrain)
# predicted_price = model.predict([[20]])
# print(predicted_price)
# accuracy = accuracy_score(data[['price']],model.predict(data[['version']]))
# print(accuracy)