"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    main()

#ВЫПОЛНЕНИЕ ЗАДАНИЯ


user_age = int(input("Сколько вам лет?  "))

if isinstance(user_age, int):

  if user_age < 7:
    print ("Детский сад")
  elif user_age <= 18:
    print ("Школа")
  elif user_age <= 23:
    print ("ВУЗ")
  elif user_age > 23:
    print ("Работа")

else:
  print("Пожалуйста, введите целое положительное число")


#Почему-то Почему отступы стали 2 пробела вместо 4х (при нажатии стандартного Tab) 

#Зачем в заданиях дано def main и все что ниже 

#Как вернуть пользователю сообщение, что нужно ввести именно целое положительное число, ошибка возникает раньше 



