import random
from morse_character_dictionary import morse


def morse_encode(word):
    """
    Функция на перевод слов в азбуку Морзе
    """

    encode = []

    for symbol in word:
        encode.append(morse[symbol])

    return encode


def get_word(words):
    """
    Функция на получение случайного слова из списка
    """

    return random.choice(words)


def print_statistics(answers):
    """
    Функция на вывод статистики
    """

    print(f"Всего задачек: {len(answers)}")
    print(f"Отвечено верно: {answers.count(True)}")
    print(f"Отвечено неверно: {answers.count(False)}")


words = ['dog', 'cat', 'rabbit', 'bird', 'pig']
answers = []

# Приветствие
print("Сегодня мы потренируемся расшифровывать морзянку.")
input("Нажмите Enter и начнем")

# Цикл вопросов
for count in range(len(words)):
    word = get_word(words)

    print(f"Слово №{count}: {morse_encode(word)}")

    user_input = input()

    if word == user_input:
      print(f"Верно, {word}!")
      answers.append(True)

    else:
      print(f"Неверно, {word}!")
      answers.append(False)

    words.remove(word)

# Вывод результатов
print_statistics(answers)





