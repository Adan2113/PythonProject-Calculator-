import os
import django
import telebot
from telebot import types
import numexpr as ne

#Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from bot_app.models import UserQuery

bot = telebot.TeleBot("8589994567:AAFPTi6tozdBbtG_kd105MMy22kaNmL9LRU")

user_screens = {}
user_drafts = {}

def get_calc_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btns = [
        "sin(", "cos(", "sqrt(", " ( ", " ) ",
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "^2", "+",
        "Очистить ❌", "Рассчитать ="
    ]
    markup.add(*[types.KeyboardButton(b) for b in btns])
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_drafts[message.chat.id] = ""
    msg = bot.send_message(message.chat.id, "Экран: `0`", reply_markup=get_calc_keyboard(), parse_mode="Markdown")
    user_screens[message.chat.id] = msg.message_id

@bot.message_handler(func=lambda message: True)
def handle_calc(message):
    chat_id = message.chat.id
    text = message.text

    if chat_id not in user_drafts:
        user_drafts[chat_id] = ""

    #обработка
    if text == "Рассчитать =":
        raw_expr = user_drafts[chat_id]
        # Подготовка формулы
        calc_expr = raw_expr.replace('sin(', 'sin((').replace('cos(', 'cos((').replace('tan(', 'tan((')
        calc_expr = calc_expr.replace(')', ') * 3.14159 / 180)')
        calc_expr = calc_expr.replace('^2', '**2')

        try:
            res_val = ne.evaluate(calc_expr).item()
            res = round(float(res_val), 4)
            user_drafts[chat_id] = str(res)

            # сейв в бд
            UserQuery.objects.create(
                user_id=chat_id,
                expression=raw_expr,
                result=str(res)
            )
        except Exception as e:
            user_drafts[chat_id] = "Ошибка"
            print(f"Ошибка расчета: {e}")

    elif text == "Очистить ❌":
        user_drafts[chat_id] = ""
    else:
        user_drafts[chat_id] += text

    # 2. обновление экрана
    display_text = user_drafts[chat_id] if user_drafts[chat_id] != "" else "0"
    try:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=user_screens[chat_id],
            text=f"Экран: `{display_text}`",
            parse_mode="Markdown"
        )
    except:
        # Если экран потерян, создаем новый
        msg = bot.send_message(chat_id, f"Экран: `{display_text}`", parse_mode="Markdown")
        user_screens[chat_id] = msg.message_id

    # 3. удаление сообщений
    try:
        bot.delete_message(chat_id, message.message_id)
    except:
        pass

bot.infinity_polling()