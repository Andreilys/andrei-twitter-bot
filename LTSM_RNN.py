import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


filename= "obama_tweets.txt"
raw_text= open(filename).read()
raw_text = raw_text.lower()
#Need to remove this so the RNN doesn't incorporate \n into its learning
raw_text = raw_text.replace("\n", " ")

#Map the characters in the corpus to integers so we can use in our neural network
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i,c in enumerate(chars))
#Create reverse mapping
int_to_char = dict((i, c) for i, c in enumerate(chars))


number_of_chars = len(raw_text)
number_of_vocab = len(chars)

#Sequence length is arbitray but I chose 140 since thats the max length of tweets
seq_length = 140
dataX = []
dataY = []
#prepare the dataset of input to output pairs encoded as integers
for i in range(0, number_of_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)

#We need to reshape so that its [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
#Normalize the variables from 0 to 1 range so its easier to learn
X = X / float(number_of_vocab)
#One hot encode the output variable
y = np_utils.to_categorical(dataY)

#Definte LTSM model based on keras
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

#Use model checkpointing to record all network weights to file each time an improvement in loss is observed
# Our best set of weights will be used to instantiate our generative model in the next section
filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

#Fit the model
model.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)


# Load network weights
filename = ""
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
