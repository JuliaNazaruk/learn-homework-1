"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""




questions_and_answers = {}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    ask_user(questions_and_answers)

#Выполнение задания

questions_and_answers_dict = {
  "Как дела": "Хорошо!", 
"Что делаешь?": "Программирую", 
"Когда освободишься": "В пятницу", 
"Куда пойдем гулять?": "В парк",
}


def small_talk (answer):
  
  return questions_and_answers_dict.get(answer, "No answer")
  

while  True:
  answer = input ("Введите вопрос, может быть я знаю ответ ")
  
  if (small_talk (answer)) != "No answer" :
    print(small_talk (answer))
    break
  else:
    print("Попробуйте еще раз")





  




 