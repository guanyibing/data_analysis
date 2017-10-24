import pandas as pd
inputfile1="train_neural_network_data.xls"
inputfile2="test_neural_network_data.xls"
outputfile="test_output_data.xls"
data_train=pd.read_excel(inputfile1)
data_test=pd.read_excel(inputfile2)
y_train=data_train.iloc[:,4].as_matrix()
x_train=data_train.iloc[:,5:17].as_matrix()
y_test=data_test.iloc[:,4].as_matrix()
x_test=data_test.iloc[:,5:17].as_matrix()
from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Activation
model=Sequential()
model.add(Dense(output_dim=17,input_dim=11))
model.add(Activation("relu"))
model.add(Dense(10,input_dim=17))
model.add(Activation("relu"))
model.add(Dense(1,input_dim=10))
model.add(Activation("sigmoid"))
model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
model.fit(x_train,y_train,nb_epoch=100,batch_size=1)
model.save_weights("net.model")
r=pd.DataFrame(model.predict_classes(x_test),columns=["预测结果"])
pd.concat([data_test.iloc[:,:5],r]).to_excel(outputfile)
