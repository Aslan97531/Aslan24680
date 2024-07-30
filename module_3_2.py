
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    a = '@'
    b = ['.com', '.ru', '.net']

    if all(a not in sender or i not in sender for i in b):
        if any (a not in recipient or i not in recipient for i in b):
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
    else:
        if sender == 'university.help@gmail.com':
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')