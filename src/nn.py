
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet
import pickle
from sklearn import metrics
from sklearn import cross_validation
import numpy

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data.pkl", "rb"))

    train_data = numpy.mat(dataset[0], numpy.float32)
    train_target = numpy.mat([[0,1] if i == 1 else [1,0] for i in dataset[1]], 
                                numpy.float32)

    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(train_data, train_target, 
                                          test_size=0.3, random_state=0)

    net1 = NeuralNet(
                layers=[  # three layers: one hidden layer
                    ('input', layers.InputLayer),
                    ('hidden1', layers.DenseLayer),
                    ('hidden2', layers.DenseLayer),
                    ('hidden3', layers.DenseLayer),
                    ('output', layers.DenseLayer),
                    ],
                # layer parameters:
                input_shape=(None, len(X_train[0])),  # 96x96 input pixels per batch
                hidden1_num_units=30,  # number of units in hidden layer
                hidden2_num_units=40,  # number of units in hidden layer
                hidden3_num_units=15,  # number of units in hidden layer
                output_nonlinearity=None,  # output layer uses identity function
                output_num_units=2,

                # optimization method:
                regression=True,
                update=nesterov_momentum,
                update_learning_rate=0.01,
                update_momentum=0.9,                
                max_epochs=4000,
                verbose=1,
                )
    
    print 'Train model.'
    
    clf = net1.fit(X_train, y_train)

    print 'Test model.'
    print 'Use cross validation.'

    print clf.score(X_test, y_test)    
    
    print 'Save model.'    
    pickle.dump(clf, open('../localdata/nn_model.pkl', 'wb'))
