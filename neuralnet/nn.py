from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.datasets.data_utils import get_file
import numpy as np
import random
import sys

# need to figure out how to use these
import speech_recognition as sr
from audiototext import audio_source


class neural_net(object):

    """
    neural_net class is the class you pass the text (or text's in future) to
    then trains the neural net then allows generations from keras
    following example file
    """

    def __init__(self, text):
        self.trained = False
        self.text = text

        # if text properply processed, build model
        if self.process_text():
            self.model = self.build_model()
        # delete this key in future
        self.recognizer = sr.Recognizer(
            key='AIzaSyASM587FctrnOddazt6LK7z80797NTckmk')

    def sample(a, temperature=1.0):
        # helper function to sample an index from a probability array
        a = np.log(a) / temperature
        a = np.exp(a) / np.sum(np.exp(a))
        return np.argmax(np.random.multinomial(1, a, 1))

    def get_file(self):
        '''need to change this to use postgres
        '''
        text = open(get_file(textfile)).read().lower()
        # print('length of textfile: ',len(text))
        return text

    def process_text(self):
        chars = set(self.text)
        print('total chars:', len(chars))
        char_indices = dict((c, i) for i, c in enumerate(chars))
        indices_char = dict((i, c) for i, c in enumerate(chars))

        maxlen = 20
        step = 3
        sentences = []
        next_chars = []
        for i in range(0, len(text) - maxlen, step):
            sentences.append(text[i: i + maxlen])
            next_chars.append(text[i + maxlen])
        # print('nb sequences:', len(sentences))

        X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
        y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
        for i, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                X[i, t, char_indices[char]] = 1
            y[i, char_indices[next_chars[i]]] = 1

        self.chars, self.X, self.y = chars, X, y
        return True

    def build_model(self, model_parameters=512):
        """
        building model:
        """

        model = Sequential()
        # input -> layer 1
        model.add(LSTM(len(chars), 512, return_sequences=True))
        model.add(Dropout(0.20))
        # use dropout on all LSTM layers: http://arxiv.org/abs/1312.4569

        # 1.5 testing
        model.add(LSTM(512, 512, return_sequences=True))
        model.add(Dropout(0.20))
        # layer 2
        model.add(LSTM(512, 256, return_sequences=True))
        model.add(Dropout(0.20))
        # layer 3
        model.add(LSTM(256, 256, return_sequences=False))
        model.add(Dropout(0.20))
        # layer 4 -> output
        model.add(Dense(256, len(chars)))
        model.add(Activation('softmax'))

        # need to compile model to fit it
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

        return model

    def train_model(self):

        # train the model, output generated text after each iteration
        for iteration in range(1, 60):
            print()
            print('-' * 50)
            print('Iteration', iteration)
            model.fit(X, y, batch_size=128, nb_epoch=1)

            start_index = random.randint(0, len(text) - maxlen - 1)

            for diversity in [0.2, 0.5, 1.0, 1.2]:
                print()
                print('----- diversity:', diversity)

                generated = ''
                sentence = text[start_index: start_index + maxlen]
                generated += sentence
                print('----- Generating with seed: "' + sentence + '"')
                sys.stdout.write(generated)

                for iteration in range(400):
                    x = np.zeros((1, maxlen, len(chars)))
                    for t, char in enumerate(sentence):
                        x[0, t, char_indices[char]] = 1.

                    preds = model.predict(x, verbose=0)[0]
                    next_index = sample(preds, diversity)
                    next_char = indices_char[next_index]

                    generated += next_char
                    sentence = sentence[1:] + next_char

                    sys.stdout.write(next_char)
                    sys.stdout.flush()
                print()


if __name__ == '__main__':
    # url = 'https://www.youtube.com/watch?v=3fbmf2IAEVM'
    a = audio_source(url=url)

    # pass the audio source a text into neural net to create model from
    net = neural_net(a.text)
    net.train_model()
