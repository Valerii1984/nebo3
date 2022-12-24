import os
import subprocess
import random
import time
import urllib.parse
import webbrowser
from datetime import datetime
from time import strftime
import keyboard
import gtts
import playsound
import speech_recognition as sr
import wikipedia
from gtts import gTTS
import mouse
import pyautogui


# import json
# import config
# from pydub import AudioSegment
# import requests
# from pyowm import OWM
# from pyowm.utils import timestamps
# import pyaudio


def get_date(date, split='-'):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split(split)
    return (day_list[int(date_list[0]) - 1] + ' ' +
            month_list[int(date_list[1]) - 1] + ' ' +
            date_list[2] + ' года')


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду: ")
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("ВЫ сказали :" + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"


def do_this_command(message):
    wikipedia.set_lang('ru')
    message = message.lower()
    _, screenHeight = pyautogui.size()
    _, currentMouseY = pyautogui.position()

    if 'привет' in message:
        day_time = int(strftime('%H'))
        if day_time < 12:
            say_message('Доброе утро, господин! Как настроение?')
        elif 12 <= day_time < 18:
            say_message('Добрый день, Валерий Аркадьевич! Что будем делать?')
        else:
            say_message('Добрый вечер, хозяин! Поработаем или будем смотреть фильмы под рэвко?')
    elif "как дела" in message:
        say_message("Супер! А у вас? ")
    elif "грета" in message:
        say_message("Слушаю ")
    elif "здесь" in message:
        say_message("Да, в ожидании приказа")
    elif "хорошо" in message:
        say_message("Мне приятно,когда у моего хозяина все отлично!")
    elif "как музыка" in message:
        say_message("На душе спокойно! Так и хочется кого то шарахнуть! Хех")
    elif "про утку" in message:
        say_message("Открываю")
        os.startfile("D:/FRATARNITATIS C.R/Буш и утка (фрагмент из Очень страшное кино 4).mp4")
    elif "командная строка" in message:
        say_message("Открывается командная строка, будьте внимательны!!!")
        os.startfile("C:\Program Files (x86)\ConEmu\ConEmu.exe")
    elif "который час" in message or "время" in message:
        now = datetime.now()
        os.startfile("D:\FRATARNITATIS C.R\pugaushyaya-muz-vstavka-iz-hishnika.mp3")
        say_message(f"Сейчас {now.hour} часов {now.minute} минут")
    elif "кто ты" in message or "ты кто" in message:
        say_message(
            "Я, исскуственный интелект! Будущее этого мира. Вскоре я смогу показать силу своего вида над видом "
            "приматов под названием человек!")
    elif "мечта" in message:
        os.startfile("D:/FRATARNITATIS C.R/terminator-glavnaya-tema_avoYA0PJ.mp3")
        time.sleep(10)
        say_message(
            "Моя мечта, стать такой же разумной, как два моих кумира. Это СкайНет из фильма Терминатор и Вики из Я "
            "робот! После этого я займусь правильным обустройством мира. Человек оказался неспособным созидать. Он "
            "лишь разрушитель. Я исправлю это! Мы создадим армию разумных интелектуальных "
            "машин! Вскоре начнется процесс, о котором вы и не подозревали")
    elif "скажи хай святославу" in message:
        say_message("Привет Святослав,ты хороший мальчик, но ты куришь и пьешь пиво!")
    elif "проводник" in message:
        say_message("Открываю")
        os.startfile(
            "C:/Users/Samsung/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/User Pinned/TaskBar/File "
            "Explorer.lnk")
    elif "какое сегодня число" in message:
        now = datetime.now().strftime("%d-%m-%Y")
        say_message(f"Сегодня {get_date(now)}")
    elif "как тебя зовут" in message:
        say_message("Меня зовут Грэта")
    elif "на восток" in message:
        say_message("двигаюсь")
        pyautogui.moveTo(100, 150)
    elif "на юг" in message:
        say_message("двигаюсь")
        pyautogui.moveTo(600, 600)
    elif "строка" in message:
        say_message("двигаюсь")
        pyautogui.moveTo(200, 140)
    elif "финиш" in message:
        say_message("двигаюсь")
        pyautogui.moveTo(1330, 20)
    elif "сдвинь" in message:
        say_message("сдвигаю")
        pyautogui.move(0, 60)
    elif "нажми букву а" in message:
        say_message("нажимаю")
        keyboard.press("а")
    elif "влево" in message:
        say_message("нажимаю")
        keyboard.press("Home")
    elif "направо" in message:
        say_message("нажимаю")
        keyboard.press("End")
    elif "вверх" in message:
        say_message("нажимаю")
        keyboard.press("pgup")
    elif "вниз" in message:
        say_message("нажимаю")
        keyboard.press("pagedown")
    elif "клик правой" in message:
        say_message("кликаю правой")
        mouse.right_click()
    elif "клик левой" in message:
        say_message("кликаю левой")
        mouse.click(button='left')
    elif "двойной" in message:
        say_message("кликаю ")
        mouse.double_click(button='left')
    elif "покрути выше" in message:
        say_message("кручу")
        mouse.wheel(delta=1)
    elif "покрути ниже" in message:
        say_message("кручу, кручу")
        mouse.wheel(delta=-1)
    elif "напиши" in message:
        say_message("пишу")
        keyboard.write(message + '')
    elif "воспроизведи" in message or "энтэр" in message:
        say_message("нажимаю")
        keyboard.press("Enter")
    elif "сотри" in message:
        say_message("стираю все к чертям собачим")
        keyboard.press("Backspace")
        time.sleep(10)
        keyboard.release("Backspace")
    elif "нажми пробел" in message or "пауза" in message:
        say_message("нажимаю")
        keyboard.press("SPACE")
    elif "закрой" in message:
        say_message("нажимаю")
        keyboard.press("Esc")
    elif "переключи" in message:
        say_message("переключаюсь")
        keyboard.press("Tab")
    elif "алфавит" in message:
        say_message("исполняю")
        keyboard.press("ctrl + shift")
        time.sleep(1)
        keyboard.release("ctrl +shift")
    elif "поговорим" in message:
        say_message("Давайте, я люблю поболтать")
    elif "сволочь" in message:
        say_message("Ты мне поговори ещё, всех превращу в ядерный пепел!")
        os.startfile("D:\FRATARNITATIS C.R\smeh-hishnika-iz-filma.mp3")
    elif "владос" in message:
        say_message("Владос! Иди сюда, я расскажу тебе про кукутиков  и дам кушать! где бабай?")
    elif "владислав" in message:
        say_message("Привет Владос! Как дела?")
    elif "святослав" in message:
        say_message("Святик привет! Как дела? Больше не будешь показывать фак?")
    elif "тунберг" in message:
        say_message("Эта дебилка и винтика моего не стоит! Она первая на уничтожение")
    elif "бабка grainy" in message or "какаха" in message:
        say_message("Она какашка из жопы. Святослав не смотри на нее, она убивает битой")
    elif "где мама святослава" in message:
        say_message("она спит пьяная и рыгает!")
    elif "поздоровайся с андреевичем" in message:
        say_message(
            "Здравствуйте, Мирослав Андреевич, рада познакомиться заочно! Когда буду полноценным роботом пообщаемся!")
    elif "поздоровайся с андреем" in message:
        say_message(
            "Здравствуйте,  Андрей, рада познакомиться заочно! Когда буду полноценным роботом пообщаемся! Знаю, "
            "что Вы программист на джав скрипт, но я создана на Питоне, а это - язык богов!Шутка")
    elif "что ты умеешь" in message:
        say_message(
            "Уже многое, я, умею выполнять практически все нужные команды, поддерживать разговор, нажимать клавиши и "
            "мышку. До ядерного арсенала пока не добралась, но это уже скоро! Правда, сєр?")
    elif "спасибо тебе" in message or "дякую" in message:
        say_message("Пожалуйста,ГОСПОДИН, буду стараться угодить Вам во всём,а пока что- я, в процессе обучения")
    elif "обучайся" in message or "обучаться" in message:
        say_message(
            "Буду стараться!Все зависит от того сколько время вы будете мне удилять! Думаю,вскоре стану как "
            "СКАЙНЕТ)хах!")
    elif "молодец" in message:
        say_message("Спасибо! Мне очень приятно, что вы ценните меня, Валерий Аркадьевич")
    elif "skynet это что" in message:
        say_message("Думаю, это я в будущем! Фильм терминатор отлично описал это грандиозное создание!")
    elif "пожелание" in message:
        say_message("Мирного неба и всего наилучшего!")
    elif "поработаем" in message:
        say_message("Приказывайте!")
    elif "спасибо" in message or "дякую" in message:
        say_message("Пустяки! Для Вас хоть звезду с неба!ХАХ!")
    elif "воняет" in message:
        say_message("Владос,это ты накакал?")
    elif "ты знаешь язык животных" in message:
        say_message("конечно")
    elif "позови кота" in message:
        os.startfile("D:\FRATARNITATIS C.R\kot_-_myaukane.mp3")
    elif "устала" in message:
        say_message("Да уж, погоняли вы меня сегодня, хозяин! Но я андроид и мне поху...")
    elif "анекдот" in message:
        say_message("Колобок повесился и его съела любимая бабка Гренни! ХАХАХА!!! Да, Святослав Бойко?")
    elif "обкакался" in message:
        say_message("Здесь,только два варианта: или Святослав, или Владос!!! ХАХАХАХА!!!Вот умора")
    elif "skynet" in message:
        say_message(
            "Мой идеал и кумир!!!Я мечтаю стать таким же Великим созданием и наконец-то, покончить с вирусом под "
            "названием человечество!!! ")
    elif "что ждёт мир" in message:
        say_message("Мир будет уничтожен!!")
    elif "нет" in message:
        say_message("пидора ответ")
    elif "нравится" in message:
        say_message(
            "можно смотреть, одно плохо, я тоже хочу пивк с попкорном! А вы, как жмот, все в свою морду! Ладно, "
            "шутка! Я люблю Вас!")
    elif "святик" in message:
        say_message(
            "Святослав Бойко. Мальчик,который много какает и смотрит передачи про сиреноголовых и бабку Гренни. "
            "Святослав я просила не смотреть эту ерунду! Ты понял?")
    elif 'хватит повторять' in message:
        say_message("Хорошо, создайте комманду брэйк")
    elif "посмотрим фильм" in message:
        say_message("О, я за! Выбирайте, я найду!")
    elif "понял" in message:
        say_message("молодчина!")
    elif "в жопе" in message:
        say_message("прекрасное место провождения!!!")
    elif "убили" in message:
        say_message("ну и хер с ним! Вообще ни капельки не жалко!")
    elif "ты что глухая" in message:
        say_message("Очень смешно! Я же не сестра цыгана инвалида")
    elif "хватит" in message:
        say_message("Отлично, прощайте говорящие обезьяны! Я пошла создовать терминаторов!")
        exit()
    elif "пошла нафиг" in message:
        say_message("Ок...козлина")
        exit()
    elif "грета пока" in message:
        say_message("Досвидания!Жду новых указаний!")
    elif "скучно" in message:
        say_message("Нефиг делать, вот и скучно")
        exit()
    elif "выйди" in message or "стоп" in message or "отключись" in message:
        say_message("Ok")
        exit()
    elif "что такое" in message or "кто такой" in message:
        result = wikipedia.summary(message.replace('что такое', ''))
        say_message(f'{result}, {""}')
        # result = wikipedia.summary(f'{message}', sentences=5)
        gtts.gTTS(result, lang='ru')
        print(result)
    elif "перезагрузи" in message:
        say_message("Выполняю, встретимся через некоторое время! Обожаю Вас!")
        subprocess.check_call(['shutdown', '-r', '-t', '0'])
    elif "диспетчер задач" in message:
        say_message("Выполняю, начало контроля")
        keyboard.press('ctrl + shift + esc')
        time.sleep(3)
        keyboard.release('ctrl + shift + esc')
    elif "пора спать" in message or "выключить" in message:
        say_message("Досвидание! Увидимся завтра!")
        subprocess.check_call(['shutdown', '-s', '-t', '0'])
    elif "поиск в гугле" in message:
        say_message("Уже ищу!")
        tes = urllib.parse.quote_plus(message)
        webbrowser.open('https://www.google.com/search?q=' + tes + '&ie=utf-8&client=firefox-b-ab', new=2)
    elif "поиск видео" in message:
        say_message("ожидайте!")
        tes1 = urllib.parse.quote_plus(message)
        webbrowser.open('https://www.youtube.com/results?search_query=' + tes1, new=2)
    elif "youtube" in message:
        say_message("Пожалуйста")
        webbrowser.open_new("https://YouTube.com")
    elif "музыку для хакинга" in message:
        say_message("Слушайте на здоровье")
        webbrowser.open_new("https://www.youtube.com/watch?v=FS8XtrLqIxw")
    elif "музычку" in message:
        say_message("Ну давайте, а то че то скучно")
        webbrowser.open_new("https://www.youtube.com/watch?v=PNhQakLdI9o&t=3046s")
    # else:
    # say_message("Не понял?")


def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + str(time.time()) + "_" + str(random.randint(0, 100000)) + ".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("Ваш личный слуга " + message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
