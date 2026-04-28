import re
from collections import defaultdict


class Word:
    #клас представляє одне слово тексту

    def __init__(self, text):
        #ініціює та зберігає слово у нижньому регістрі
        self.text = text.lower()

    def __repr__(self):
    #повертає текстове представлення слова
        return self.text

    def __eq__(self, other):
    #перевірка 2 слів на співпадіння
        return isinstance(other, Word) and self.text == other.text

    def __hash__(self):
    # потрібно щоб слова можна було використовувати в set і як ключ у dict
        return hash(self.text)

class Sentence:
#клас представляє речення

    def __init__(self, sentence_text):
        #ініціалізація речення

        # зберігається оригінальне речення щоб потім вивести
        self.original = sentence_text

        # парсимо слова у список об'єктів Word
        self.words = self._parse_words(sentence_text)

    def _parse_words(self, text):
        #виділяємо слова у реченні
        words = re.findall(r'\b\w+\b', text.lower())
        return [Word(w) for w in words]

    def get_word_set(self):
    #повертаэ множину слів речення
    #повертаэмо в frozenset щоб проігнорити поряд та щоб використати як ключ для словника
        return frozenset(self.words)

    def __repr__(self):
        #повертаэ оригінальний текст речення
        return self.original


class Text:
    #представляэ весь текст

    def __init__(self, text):
    #ініціалізація тексту
        self.sentences = self._parse_sentences(text)

    def _parse_sentences(self, text):
    #розбиваємо текст на речення
        sentences = re.split(r'[.!?]+', text)

        #видаляємо порожні рядки та пробіли
        return [Sentence(s.strip()) for s in sentences if s.strip()]


class Program:


    @staticmethod
    def calculate_c_values(nzk):
    # обчислення варіанту
        return nzk % 3, nzk % 17

    @staticmethod
    def normalize_text(text):
    #видалення лишніх пробілів чи табів
        return ' '.join(text.split())

    @staticmethod
    def find_max_sentences(text_obj):
    #знаходимо найбільшу групу речень які складаються з однакових слів
        groups = defaultdict(list)

        #групування речень
        for sentence in text_obj.sentences:
            key = sentence.get_word_set()
            groups[key].append(sentence)

        # пошук найбільшої групи
        max_group = []
        for group in groups.values():
            if len(group) > len(max_group):
                max_group = group

        return max_group

    @staticmethod
    def main():
        try:
            # номер залікової книжки
            nzk = 5202

            # вхідний текст
            text = (
                "Hello world! "
                "World hello. "
                "Hi World. "
                "Test Hello World. "
                "Word Helo"
            )

            # обчислення варіантів
            c3, c17 = Program.calculate_c_values(nzk)

            print(f"C3 = {c3}")
            print(f"C17 = {c17}")

            # перевірка варіанту
            if c3 != 0 or c17 != 0:
                print("Неправильний варіант")
                return

            #нормалізація тексту
            normalized = Program.normalize_text(text)

            #створення об'єкта Text (композиція класів)
            text_obj = Text(normalized)

            #пошук результату
            result = Program.find_max_sentences(text_obj)

            print("\nРезультат:")
            print("Кількість речень:", len(result))

            for i, sentence in enumerate(result, 1):
                print(f"{i}. {sentence}")

        except Exception as e:
            print("Error:", e)


#вхід
if __name__ == "__main__":
    Program.main()
