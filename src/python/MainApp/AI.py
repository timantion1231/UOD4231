import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import string

class ArtInt:

    train_path = f'resources/datasets/train.csv'
    test_path = f'resources/datasets/test.csv'

    train_text = None
    test_text = None
    train_emo = None
    test_emo = None

    max_words = 10000
    max_len = 100
    embedding_dim = 100
    num_classes = 7  # no emotion (0), anger (1), disgust (2), fear (3), happiness (4), sadness (5), surprise (6)

    def __init__(self):
        self.prepare_data()
        self.fit_model()


    def get_emotion(self, text):
        return "pass"

    def prepare_data(self):
        data_train = pd.read_csv(self.train_path)
        data_test = pd.read_csv(self.test_path)

        self.train_text = data_train.dialog.loc[data_train.index[0]]
        self.train_text = self.train_text.split('\n')

        self.test_text = data_test.dialog.loc[data_test.index[0]]
        self.test_text = self.test_text.split('\n')
        print(self.train_text)
        print(self.test_text)
        print('self.test_emo')

        self.train_emo = data_train.emotion.loc[data_train.index[0]]
        self.train_emo = self.train_emo.split(' ')

        self.test_emo = data_test.emotion.loc[data_test.index[0]]
        self.test_emo = self.test_emo.split(' ')

        for i in range(len(self.train_emo)):
            self.train_emo[i] = self.train_emo[i].translate(str.maketrans('', '', string.punctuation))
            self.train_emo[i] = int(self.train_emo[i])

        for i in range(len(self.test_emo)):
            self.test_emo[i] = self.test_emo[i].translate(str.maketrans('', '', string.punctuation))
            self.test_emo[i] = int(self.test_emo[i])
        print('self.train_emo')

    def fit_model(self):
        # Токенизируйте тексты
        tokenizer = Tokenizer(num_words=self.max_words)
        tokenizer.fit_on_texts(self.train_text)

        train_sequences = tokenizer.texts_to_sequences(self.train_text)
        test_sequences = tokenizer.texts_to_sequences(self.test_text)

        # Добавьте нулевую вставку для достижения одинаковой длины последовательностей
        train_padded = pad_sequences(train_sequences, maxlen=self.max_len)
        test_padded = pad_sequences(test_sequences, maxlen=self.max_len)

        # Преобразуйте метки в массив NumPy
        self.train_emo = np.array(self.train_emo[:len(train_padded)])  # Убедитесь, что количество примеров совпадает
        self.test_emo = np.array(self.test_emo[:len(test_padded)])  # Убедитесь, что количество примеров совпадает

        # Определите архитектуру модели
        model = Sequential()
        model.add(Embedding(input_dim=self.max_words, output_dim=self.embedding_dim))
        model.add(LSTM(units=32, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(units=self.num_classes, activation='softmax'))

        # Определите оптимизатор и функцию потерь
        optimizer = Adam()
        loss = 'sparse_categorical_crossentropy'
        metrics = ['accuracy']

        model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

        # Обучите модель
        model.fit(train_padded, self.train_emo, validation_data=(test_padded, self.test_emo), epochs=10, batch_size=32)
