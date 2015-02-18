
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet
import numpy
import pickle
from sklearn import cross_validation
from sklearn import preprocessing

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data_0.pkl", "rb"))

    train_data = numpy.mat(dataset[0], numpy.float32)
    train_target = numpy.mat([[0, 1] if i == 1 else [1, 0] for i in dataset[1]], 
                             numpy.float32)
#    train_target = numpy.mat([[1] if i == 1 else [0] for i in dataset[1]], 
#                             numpy.float32)

    #Scaling the data
    print 'Scaling the data.'
    min_max_scaler = preprocessing.MinMaxScaler()
    train_data = numpy.mat(min_max_scaler.fit_transform(train_data), 
                           numpy.float32)

    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(train_data, train_target, 
                                          test_size=0.3, random_state=0)

    print 'Build NN.'
    net1 = NeuralNet(
                     layers=[
                     ('input', layers.InputLayer),
                     ('hidden1', layers.DenseLayer),
#                     ('dropout1', layers.DropoutLayer),
                     ('hidden2', layers.DenseLayer),
#                     ('dropout2', layers.DropoutLayer),
                     ('hidden3', layers.DenseLayer),
#                     ('dropout3', layers.DropoutLayer),
                     ('hidden4', layers.DenseLayer),
#                     ('dropout4', layers.DropoutLayer),
                     ('hidden5', layers.DenseLayer),
                     ('hidden6', layers.DenseLayer),
                     ('hidden7', layers.DenseLayer),
                     ('hidden8', layers.DenseLayer),
                     ('hidden9', layers.DenseLayer),
                     ('hidden10', layers.DenseLayer),
                     ('output', layers.DenseLayer),
                     ],
                     # layer parameters:
                     input_shape=(None, len(X_train[0])),
                     hidden1_num_units=30,
#                     dropout1_p=0.1,
                     hidden2_num_units=90,
#                     dropout2_p=0.2,
                     hidden3_num_units=240,
#                     dropout3_p=0.3,
                     hidden4_num_units=340,
#                     dropout4_p=0.5,
                     hidden5_num_units=680,
                     hidden6_num_units=1000,
                     hidden7_num_units=500,
                     hidden8_num_units=240,
                     hidden9_num_units=90,
                     hidden10_num_units=30,
                     output_nonlinearity=None,
                     output_num_units=2,

                     # optimization method:
                     regression=True,
                     update=nesterov_momentum,
                     update_learning_rate=0.01,
                     update_momentum=0.9, 
                     max_epochs=5000,
                     verbose=1,
                     )
    
    print 'Train model.'
    
    clf = net1.fit(X_train, y_train)

    print 'Test model.'
    print 'Use cross validation.'

    print clf.score(X_test, y_test)    
    
    print 'Save model.'    
    pickle.dump(clf, open('../localdata/nn_model.pkl', 'wb'))
