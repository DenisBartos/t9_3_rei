import random


class T9:
    def __init__(self):
        self.dictionary = {
            '2': ['а', 'б', 'в'],
            '3': ['г', 'д', 'е', 'ё', 'ж', 'з'],
            '4': ['и', 'й', 'к', 'л', 'м'],
            '5': ['н', 'о', 'п', 'р', 'с'],
            '6': ['т', 'у', 'ф', 'х'],
            '7': ['ц', 'ч', 'ш', 'щ'],
            '8': ['ъ', 'ы', 'ь'],
            '9': ['э', 'ю', 'я']
        }


        # Укажите путь к файлу словаря ru_RU
        self.word_list = "ru.json"
        self.word_frequency = {word: random.randint(1, 10) for word in self.word_list}  # Генерация случайной частоты

    def get_words(self, input_sequence):
        if not input_sequence:
            return []

        words = ['']
        for digit in input_sequence:
            if digit in self.dictionary:
                new_words = []
                for word in words:
                    for letter in self.dictionary[digit]:
                        new_words.append(word + letter)
                words = new_words
        return words

    def suggest_words(self, input_sequence):
        possible_words = self.get_words(input_sequence)
        ranked_words = sorted(possible_words, key=lambda x: self.word_frequency.get(x, 0), reverse=True)
        return ranked_words

def main():
    t9 = T9()
    user_input = input("Введите последовательность цифр (например, '7483' для 'школа'): ")
    suggestions = t9.suggest_words(user_input)
    print("Возможные слова:", suggestions)

if __name__ == "__main__":
    main()
