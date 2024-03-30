from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

class Tokens:
    def get_tokens_from_text(texts):
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', texts)
        tokenizer = Tokenizer()
        # Обучение токенизатора на тексте
        tokenizer.fit_on_texts(sentences)

        # Преобразование текста в последовательности чисел
        sequences = tokenizer.texts_to_sequences(sentences)



        # Получение словаря слов и их индексов
        word_index = tokenizer.word_index

        return sequences, word_index

    def __get_text_from_tokens(self, tokens):
        pass

    def get_emotion_from_tokens(self, tokens):
        pass



