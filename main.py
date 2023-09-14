import telebot
from telebot import types
from telebot.types import WebAppInfo
import info

Bot = telebot.TeleBot('6500578632:AAFhL9Kg1rowoC2IgH5nKEIXnvHYevX2Ces')


@Bot.message_handler(commands=['start'])
def start(message):
    serviceBTN = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Услуги')
    serviceBTN.add(btn1)
    Bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} 👋')
    Bot.send_message(message.chat.id, 'Ты можешь ознакомиться с моими услугами по кнопке ниже 👇', reply_markup=serviceBTN)

@Bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Услуги':
        serviceBTNLine = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Sbtn1 = types.KeyboardButton('✨ Реконструкция волос')
        serviceBTNLine.row(Sbtn1)
        Sbtn2 = types.KeyboardButton('Стрижки')
        Sbtn3 = types.KeyboardButton('Окрашивание')
        serviceBTNLine.row(Sbtn2, Sbtn3)
        Sbtn4 = types.KeyboardButton('🌟 Косметика и домашний уход')
        serviceBTNLine.row(Sbtn4)
        Sbtn5 = types.KeyboardButton('‼ Акции ‼')
        serviceBTNLine.row(Sbtn5)
        Bot.send_message(message.chat.id, "Выбирете одну из услуг ниже 👇", reply_markup=serviceBTNLine)


    elif message.text == '✨ Реконструкция волос':
        serviceBTNLine2 = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        Sbtn1 = types.KeyboardButton('Кератин')
        Sbtn2 = types.KeyboardButton('Ботокс')
        serviceBTNLine2.row(Sbtn1, Sbtn2)
        Sbtn3 = types.KeyboardButton('Холодный ботокс')
        Sbtn4 = types.KeyboardButton('Многоступенчатый уход')
        serviceBTNLine2.row(Sbtn3, Sbtn4)
        Sbtn5 = types.KeyboardButton('Детокс-пилинг + увлажнение волос')
        serviceBTNLine2.row(Sbtn5)
        Back = types.KeyboardButton('Главное меню')
        serviceBTNLine2.row(Back)
        Bot.send_message(message.chat.id, "Выбирете одну из реконструкций 👇", reply_markup=serviceBTNLine2)
    elif message.text == 'Кератин':
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='kiratin_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='kiratin_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(message.chat.id, "Процедура кератин", reply_markup=serviceBTNLine)
    elif message.text == 'Ботокс':
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='botoks_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='botoks_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(message.chat.id, "Процедура ботокс", reply_markup=serviceBTNLine)
    elif message.text == 'Холодный ботокс':
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='icebotoks_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='icebotoks_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(message.chat.id, "Процедура Холодный ботокс", reply_markup=serviceBTNLine)
    elif message.text == 'Многоступенчатый уход':
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='mnogostyp_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='mnogostyp_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(message.chat.id, "Процедура Многоступенчатый уход (тотальная реконструкция)", reply_markup=serviceBTNLine)
    elif message.text == 'Детокс-пилинг + увлажнение волос':
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='detoks_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='detoks_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(message.chat.id, "Процедура Детокс-пилинг + увлажнение волос", reply_markup=serviceBTNLine)

    elif message.text == 'Стрижки':
        serviceBTNLine2 = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('Стоимость', callback_data='haircuts_price')
        serviceBTNLine2.row(Sbtn1)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine2.row(Sbtn3)
        Bot.send_message(message.chat.id, "Вот информация по стрижкам", reply_markup=serviceBTNLine2)

    elif message.text == 'Окрашивание':
        serviceBTNLine2 = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('Airtouch', callback_data='Airtouch')
        serviceBTNLine2.row(Sbtn1)
        Sbtn2 = types.InlineKeyboardButton('Тотал блонд', callback_data='TotalBlond')
        serviceBTNLine2.row(Sbtn2)
        Bot.send_message(message.chat.id, "Виды окрашивания", reply_markup=serviceBTNLine2)

    elif message.text == '🌟 Косметика и домашний уход':
        serviceBTNLine2 = types.InlineKeyboardMarkup()
        serviceBTNLine2.add(types.InlineKeyboardButton('Открыть каталог', web_app=WebAppInfo(url="https://nastyahair.ru/katalog")))
        Bot.send_message(message.chat.id, "Каталог продукции для ухода за собой", reply_markup=serviceBTNLine2)

    elif message.text == '‼ Акции ‼':
        serviceBTNLine2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Sbtn1 = types.KeyboardButton('🥳 Скидка Дня Рождения')
        Sbtn2 = types.KeyboardButton('🤗 Скидка на 3-е посещение')
        serviceBTNLine2.row(Sbtn1, Sbtn2)
        Sbtn3 = types.KeyboardButton('Главное меню')
        serviceBTNLine2.row(Sbtn3)
        Bot.send_message(message.chat.id, "Выбирите акцию для просмотра подробной информации", reply_markup=serviceBTNLine2)
    elif message.text == '🥳 Скидка Дня Рождения':
        Bot.send_message(message.chat.id, "🥳")
        Bot.send_message(message.chat.id, "В честь Дня Рождения: скидка 15% за неделю до/после")
    elif message.text == '🤗 Скидка на 3-е посещение':
        Bot.send_message(message.chat.id, "🤗")
        Bot.send_message(message.chat.id, "Каждое 3-е посещение скидка 10% от прайса")


    elif message.text == 'Главное меню':
        serviceBTNLine = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Sbtn1 = types.KeyboardButton('✨ Реконструкция волос')
        serviceBTNLine.row(Sbtn1)
        Sbtn2 = types.KeyboardButton('Стрижки')
        Sbtn3 = types.KeyboardButton('Окрашивание')
        serviceBTNLine.row(Sbtn2, Sbtn3)
        Sbtn4 = types.KeyboardButton('🌟 Косметика и домашний уход')
        serviceBTNLine.row(Sbtn4)
        Sbtn5 = types.KeyboardButton('‼ Акции ‼')
        serviceBTNLine.row(Sbtn5)
        Bot.send_message(message.chat.id, "Вы вернулись на главное меню, выбирете одну из услуг ниже 👇", reply_markup=serviceBTNLine)





@Bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
# Кератин
    if call.data == 'keratin':
        Bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='kiratin_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='kiratin_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(call.message.chat.id, "Процедура кератин", reply_markup=serviceBTNLine)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'kiratin_info':
        Bot.send_photo(call.message.chat.id, open('./keratin_info/photo_2023-08-15_16-01-23.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='keratin')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, info.kiratin_info_text, reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'kiratin_price':
        Bot.send_photo(call.message.chat.id, open('./keratin_info/Прайс Кератин.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='keratin')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, "Прайс на кератин", reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)

# Ботокс
    elif call.data == 'botoks':
        Bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='botoks_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='botoks_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(call.message.chat.id, "Процедура ботокс", reply_markup=serviceBTNLine)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'botoks_info':
        Bot.send_photo(call.message.chat.id, open('./botoks_info/photo_2023-08-15_16-01-18.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='botoks')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, info.botoks_info_text, reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'botoks_price':
        Bot.send_photo(call.message.chat.id, open('botoks_info/Ботокс прайс.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='botoks')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, "Прайс на ботокс", reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)

#Холодный ботокс
    elif call.data == 'icebotoks':
        Bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='icebotoks_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='icebotoks_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(call.message.chat.id, "Процедура Холодный ботокс", reply_markup=serviceBTNLine)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'icebotoks_info':
        Bot.send_photo(call.message.chat.id, open('./icebotoks_info/photo_2023-08-21_13-44-01.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='icebotoks')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, info.icebotoks_info_text, reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'icebotoks_price':
        Bot.send_photo(call.message.chat.id, open('./icebotoks_info/Холодный ботокс прайс.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='icebotoks')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, "Прайс на холодный ботокс", reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)

#Многоступенчатый уход (тотальная реконструкция)
    elif call.data == 'mnogostyp':
        Bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='mnogostyp_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='mnogostyp_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(call.message.chat.id, "Процедура Многоступенчатый уход (тотальная реконструкция)", reply_markup=serviceBTNLine)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'mnogostyp_info':
        Bot.send_photo(call.message.chat.id, open('./mnogostyp_info/M78A9566мини.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='mnogostyp')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, info.mnogostup_info_text, reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'mnogostyp_price':
        Bot.send_photo(call.message.chat.id, open('./mnogostyp_info/Реконстукция прайс.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='mnogostyp')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, "Прайс на Многоступенчатый уход (тотальная реконструкция)", reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)

#Детокс-пилинг + увлажнение волос
    elif call.data == 'detoks':
        Bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('О процедуре', callback_data='detoks_info')
        Sbtn2 = types.InlineKeyboardButton('Прайс', callback_data='detoks_price')
        serviceBTNLine.row(Sbtn1, Sbtn2)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(call.message.chat.id, "Процедура Детокс-пилинг + увлажнение волос", reply_markup=serviceBTNLine)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'detoks_info':
        Bot.send_photo(call.message.chat.id, open('./detoks_info/photo_2023-08-21_11-53-52.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='detoks')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, info.detox_info_text, reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'detoks_price':
        Bot.send_photo(call.message.chat.id, open('./detoks_info/Пилинг прайс.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='detoks')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, "Прайс на Детокс-пилинг + увлажнение волос", reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)


#Стрижки
    elif call.data == 'haircuts':
        Bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('Стоймость', callback_data='haircuts_price')
        serviceBTNLine.row(Sbtn1)
        Sbtn3 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        serviceBTNLine.row(Sbtn3)
        Bot.send_message(call.message.chat.id, "Вот информация по стрижкам", reply_markup=serviceBTNLine)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'haircuts_price':
        Bot.send_photo(call.message.chat.id, open('./detoks_info/Пилинг прайс.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn = types.InlineKeyboardButton('Назад', callback_data='haircuts')
        BtnKeratin1.add(KBtn)
        Bot.send_message(call.message.chat.id, "Прайс на стрижки", reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)

#Окрашивание
    elif call.data == 'coloring':
        Bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        serviceBTNLine = types.InlineKeyboardMarkup()
        Sbtn1 = types.InlineKeyboardButton('Airtouch', callback_data='Airtouch')
        serviceBTNLine.row(Sbtn1)
        Sbtn2 = types.InlineKeyboardButton('Тотал блонд', callback_data='TotalBlond')
        serviceBTNLine.row(Sbtn2)
        Bot.send_message(call.message.chat.id, "Виды окрашивания", reply_markup=serviceBTNLine)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'Airtouch':
        Bot.send_photo(call.message.chat.id, open('./coloring/Airtouch.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn1 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        BtnKeratin1.add(KBtn1)
        KBtn2 = types.InlineKeyboardButton('Назад', callback_data='coloring')
        BtnKeratin1.add(KBtn2)
        Bot.send_message(call.message.chat.id, info.Coloring_airtouch, reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'TotalBlond':
        Bot.send_photo(call.message.chat.id, open('./coloring/Тоталблонд.jpg', 'rb'))
        BtnKeratin1 = types.InlineKeyboardMarkup()
        KBtn1 = types.InlineKeyboardButton('Записаться', web_app=WebAppInfo(url="https://dikidi.net/1203486"))
        BtnKeratin1.add(KBtn1)
        KBtn2 = types.InlineKeyboardButton('Назад', callback_data='coloring')
        BtnKeratin1.add(KBtn2)
        Bot.send_message(call.message.chat.id, info.Coloring_totalblond, reply_markup=BtnKeratin1)
        Bot.delete_message(call.message.chat.id, call.message.message_id)



Bot.infinity_polling()