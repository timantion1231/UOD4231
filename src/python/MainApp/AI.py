from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

class ArtInt:
    def get_tokens_from_text(self, texts):
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

    def __get_emotion_from_tokens(self, tokens):
        pass

    def get_emotion(self, text):
        tokens, word_index = self.get_tokens_from_text(text)
        print(tokens, '\n', '---------------', '\n', word_index)
        return "pass"

