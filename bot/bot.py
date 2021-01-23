import telebot
import time

from account.models import Mentor, User
from bot.models import UserBot
from bot.config import States, TOKEN
from bot.dbworker import get_state, set_state
from bot.static_content_bot import dct
from course.models import Course, ContactUs

bot = telebot.TeleBot(
    token=TOKEN
)
manager_id = 1013917463
admin_id = [933705953, 536563573]


def get_user(chat_id, username):
    user, _ = UserBot.objects.get_or_create(chat_id=chat_id)

    if username != user.username:
        if username is None:
            username = 'None'
        user.username = username
        user.save()
    return user, _


@bot.message_handler(
    func=lambda message: message.text in ['🎛Asosiy Menyu', '🎛Главное меню', '🎛Main Menu'])
def back(message):
    start_message(message)


def get_markup_menu(chat_id, username):
    user, _ = get_user(chat_id, username)
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    buttons = [
        telebot.types.KeyboardButton(text=dct[user.language_bot]['📚Kurslar']),
        telebot.types.KeyboardButton(text=dct[user.language_bot]["👨‍💻O'qituvchilar"]),
        telebot.types.KeyboardButton(text=dct[user.language_bot]['📍Manzilimiz'])
    ]
    markup.add(*buttons)
    buttons = [
        telebot.types.KeyboardButton(text=dct[user.language_bot]['ℹ️Biz haqimizda']),
        telebot.types.KeyboardButton(text=dct[user.language_bot]["📱Biz bilan bog'lanish"]),
        telebot.types.KeyboardButton(text=dct[user.language_bot]["⚙️Tilni o'zgartirish"])
    ]
    markup.add(*buttons)
    markup.add(
        telebot.types.KeyboardButton(text=dct[user.language_bot]['📧Adminga murojat'])
    )
    if chat_id in admin_id:
        markup.add(
            telebot.types.KeyboardButton(text=dct[user.language_bot]['✉ Yangilik yaratish']),
        )
    return markup


def get_markup_change_language():
    markup = telebot.types.InlineKeyboardMarkup()
    buttons = [
        telebot.types.InlineKeyboardButton(text='🇺🇿UZ', callback_data='UZ'),
        telebot.types.InlineKeyboardButton(text='🇷🇺RU', callback_data='RU'),
        telebot.types.InlineKeyboardButton(text='🇬🇧EN', callback_data='EN')
    ]
    markup.row(*buttons)
    return markup


@bot.callback_query_handler(func=lambda call: True and call.data in ['UZ', 'RU', 'EN'])
def lang(call):
    user, _ = get_user(call.from_user.id, call.from_user.username)
    user.language_bot = call.data
    user.save()
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.id)
    markup = get_markup_menu(chat_id=call.from_user.id, username=call.from_user.username)
    if call.from_user.id == admin_id:
        markup.add(
            telebot.types.KeyboardButton(text=dct[user.language_bot]['✉ Yangilik yaratish']),
        )
    bot.send_message(
        chat_id=call.from_user.id,
        text=dct[user.language_bot]['Menyu elementlaridan birini tanlang'],
        reply_markup=markup
    )


@bot.message_handler(
    func=lambda message: message.text in ['📧Adminga murojat', '📧Связатся с администратором', '📧Contact with admin'])
def contact_admin(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    set_state(
        key=message.chat.id,
        value=States.CONTACT_ADMIN.value
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot][
            "Ushbu bo'limda siz fikr va takliflaringizni administratorga qoldirishingiz mumkin.\nFikr va taklifaringizni yozib qoldiring."
        ]
    )


@bot.message_handler(func=lambda message: get_state(key=message.chat.id) == States.CONTACT_ADMIN.value)
def message_contact_admin(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot][
            "Xabar muvaffaqiyatli qo'shildi✅\n\nLoyihamizni rivojlantirishga qo'shgan hissangiz uchun tashakkur."]
    )
    for item in admin_id:
        bot.send_message(
            chat_id=item,
            text="@" + message.chat.username + "\n" + message.text
        )
    start_message(message)


@bot.callback_query_handler(func=lambda call: True and call.data in ['cancel', 'send'])
def correct_news(call):
    user, _ = get_user(call.from_user.id, call.from_user.username)
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.id)
    markup = get_markup_menu(call.from_user.id, call.from_user.username)
    if call.from_user.id == admin_id:
        markup.add(
            telebot.types.KeyboardButton(text=dct[user.language_bot]['✉ Yangilik yaratish']),
        )
    if call.data == 'cancel':
        correct = dct[user.language_bot]["Bekor qilindi❌"]
    else:
        send_news(call.message.text)
        correct = dct[user.language_bot]["Yangiliklar muvaffaqiyatli qo'shildi✅"]
    set_state(
        key=call.from_user.id,
        value=States.START.value
    )
    bot.send_message(
        chat_id=call.from_user.id,
        text=correct + '\n' + dct[user.language_bot]['Menyu elementlaridan birini tanlang'],
        reply_markup=markup
    )


def send_news(text):
    users = UserBot.objects.all()
    for item in users:
        try:
            bot.send_message(
                chat_id=item.chat_id,
                text=text
            )
            time.sleep(0.05)
        except Exception:
            pass


@bot.message_handler(func=lambda message: message.text in ['✉ Yangilik yaratish', '✉ Добавить новость', '✉ Add News'])
def add_news(message):
    if message.chat.id in admin_id:
        user, _ = get_user(message.chat.id, message.chat.username)
        set_state(
            key=message.chat.id,
            value=States.SEND_NEWS.value
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=dct[user.language_bot][
                "Yaxshi! Yangiliklar faqat matndan iborat bo'lishi kerak\nMenga sms yozing va men barcha foydalanuvchilarga yangiliklar to'g'risida xabar beraman"]
        )


@bot.message_handler(func=lambda message: get_state(key=message.chat.id) == States.SEND_NEWS.value)
def get_news(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    markup = telebot.types.InlineKeyboardMarkup()
    buttons = [
        telebot.types.InlineKeyboardButton(text=dct[user.language_bot]['Bekor qilish❌'], callback_data='cancel'),
        telebot.types.InlineKeyboardButton(text=dct[user.language_bot]['Yuborish✅'], callback_data='send')
    ]
    markup.add(*buttons)
    bot.send_message(
        chat_id=message.chat.id,
        text=message.text,
        reply_markup=markup,
    )


# Начало
@bot.message_handler(
    func=lambda message: message.text in ["📚Kurslar", "📚Курсы", "📚Courses"])
def course_list(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    set_state(
        key=message.chat.id,
        value=States.COURSE.value
    )
    courses = Course.objects.all()
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    buttons = []
    for course in courses:
        buttons.append(telebot.types.KeyboardButton(text=course.name))
    buttons.append(telebot.types.KeyboardButton(text=dct[user.language_bot]['🎛Asosiy Menyu']))
    markup.add(*buttons)
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot]['Darsni tanlang'],
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: get_state(key=message.chat.id) == States.COURSE.value)
def course_detail(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    try:
        course = Course.objects.get(name__iexact=message.text)
        bot.send_photo(
            chat_id=message.chat.id,
            photo=course.image,
            caption=course.name + '\n' + course.info,
            reply_markup=markup,
        )
    except Course.DoesNotExist:
        bot.send_message(
            chat_id=message.chat.id,
            text=dct[user.language_bot]["Menyu elementlaridan birini tanlang"]
        )


@bot.message_handler(func=lambda message: message.text in ["👨‍💻O'qituvchilar", "👨‍💻Учителя", "👨‍💻Mentors"])
def mentor_list(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    mentors = Mentor.objects.all()
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    buttons = []
    for mentor in mentors:
        buttons.append(telebot.types.KeyboardButton(text=mentor.user.get_full_name()))
    buttons.append(telebot.types.KeyboardButton(text=dct[user.language_bot]['🎛Asosiy Menyu']))
    markup.add(*buttons)
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot]['Qaysi o`qituvchi haqida ma`lumot olmoqchisiz?'],
        reply_markup=markup
    )
    set_state(
        key=message.chat.id,
        value=States.MENTOR.value
    )


@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.MENTOR.value)
def mentor_detail(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    try:
        first_name, last_name = message.text.split()
        user = User.objects.get(first_name__iexact=first_name, last_name__iexact=last_name)
        bot.send_photo(
            chat_id=message.chat.id,
            photo=user.mentor.image,
            caption=user.get_full_name() + '\n' + user.mentor.info + '\n' + user.email,
        )
    except Mentor.DoesNotExist or ValueError:
        bot.send_message(
            chat_id=message.chat.id,
            text=dct[user.language_bot]['Iltimos ro`yhatdaki o`qituvchilardan birini tanlang']
        )


@bot.message_handler(func=lambda message: message.text in ["📍Manzilimiz", "📍Наш адресс", "📍Address"])
def get_location(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    latitude = 41.538737
    longitude = 60.633833
    bot.send_location(
        message.chat.id,
        latitude,
        longitude
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot][
            "Manzil: Urganch shahri, Yoshlik ko'chasi 26-uy\nMo'ljal:Urganch temir yo'l vokzali"]
    )


@bot.message_handler(func=lambda message: message.text in ["ℹ️Biz haqimizda", "ℹО нас", "ℹ️About Us"])
def get_info(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    text = """
        KISS – Khorezm Innovations and Software Solutions
        
        IT-Academy (Bootcamp)
        
        Xozirgi kunda “KISS – Khorezm Innovations and Software Solutions” MJCH tomonidan turli sohalar uchun dasturiy ta`minotlar yaratilmoqda, jamiyat hodimlari turli xalqaro firma va kompaniyalar uchun ishlab (Outsourcing, Freelancing) kelishmoqda. Shuningdek, dasturlashni  xalqaro darajada o`rgatuvchi IT-akademiya tashkil qilingan bo`lib u yerda talabalar va o`rganuvchilar turli hil dasturlash texnologiyalarini o`rgangan holda turli hil dasturiy loyihalar amalga oshirishni o`rganishmoqda. Markazda dasturlashni o`rgatish ingliz tilida va dasturiy ta`minotlar yaratish xalqaro standartlar asosida tashkil etilgan.
        
        Jamiyat xodimlarining 8 tasi chet el firma va kompaniyalari uchun masofadan turib dasturchi sifatida ishlab kelishmoqda. Jamiyatda tashkil qilingan IT-akademiyada esa Web dasturlash (PHP, JavaScript, Laravel, Yii2, Django, vhk), Algoritmlash, Dasturiy loyixalarni boshqarish (Proyekt Menejment), Java tilida dasturlash (Spring Boot) va Mobil qurilmalar uchun dasturiy ta`minotlar yaratish (Android, React Native, iOS), Python tilida dasturlash va Robotatexnika dasturlash (IoT – Internet of Things) yo`nalishlarida o`quv kurslari tashkil etilgan.    
        
        E`tiborga loyiqi shundan iboratki, barcha kurslarda allaqachon chet el kompaniyalarida ishlayotgan, ko`p yillik tajribaga ega, PhD (Doctor of Phylosophy) va magistr darajasiga ega bo`lgan hamda chet elda tajriba orttirib kelgan mutaxassislar tomonidan o`qitish tashkil etilgan. Bunda, mashg`ulotlar «Birinchi, Muammo (Problem First)» va «bajarish orqali o`rganish (Learning by Doing)» prinsipi asosida o`tiladi. Kurslar bitiruvchilarini Senior darajasidagi dasturchilar bo`lib yetishadi va ularni kompaniya va firmalarga dasturchi sifatida ishga joylash bo`yicha amaliy yordam beriladi.
        
        “KISS – Khorezm Innovations and Software Solutions” MCHJ "IT-PARK UZBEKISTAN"  rezidenti hisoblanadi.
        """
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot][text]
    )


# Конец

contact_us = ContactUs()


@bot.message_handler(
    func=lambda message: message.text in ["📱Biz bilan bog'lanish", "📱Связаться с нами", "📱Contact Us"])
def contact_as(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    try:
        obj = ContactUs.objects.get(
            chat_id=message.chat.id,
        )
        set_state(
            key=message.chat.id,
            value=States.START.value
        )
        if obj.check_box:
            obj.check_box = False
            obj.save()
            bot.send_message(
                chat_id=message.chat.id,
                text=dct[user.language_bot][
                    'Arizangiz uchun rahmat, menedjerlarimiz siz bilan tez orada bog`lanishadi.']
            )
            bot.send_message(
                chat_id=manager_id,
                text='Name: ' + obj.full_name + '\n' + 'Phone number: ' + obj.phone_number + '\n' + 'Course: ' + str(
                    obj.course.name) + '\n' + 'Date: ' + str(obj.date)[:20]
            )
            start_message(message)
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text=dct[user.language_bot][
                    'Sizning so`rovingiz ko`rib chiqilmoqda, iltimos menedjerlar qo`ng`iroqini kuting']
            )
    except ContactUs.DoesNotExist:
        try:
            contact_us.pk = ContactUs.objects.last().pk + 1
        except:
            contact_us.pk = message.chat.id
        contact_us.chat_id = message.chat.id
        keyboard = telebot.types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            one_time_keyboard=True
        )
        buttons = [
            telebot.types.KeyboardButton(text=dct[user.language_bot]["📱Telefon raqamimni yuborish"],
                                         request_contact=True),
            telebot.types.KeyboardButton(text=dct[user.language_bot]['🎛Asosiy Menyu'])
        ]
        keyboard.add(*buttons)
        bot.send_message(
            chat_id=message.chat.id,
            text=dct[user.language_bot]['Siz bilan bog`lanish uchun telefon raqamingizni yuboring'],
            reply_markup=keyboard
        )
        set_state(
            key=message.chat.id,
            value=States.SEND_CONTACT.value
        )


@bot.message_handler(content_types=['contact'],
                     func=lambda message: get_state(message.chat.id) == States.SEND_CONTACT.value)
def send_contact(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    if message.chat.id != message.contact.user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text=dct[user.language_bot]['Uzingni kontaktingizni yuboring!!']
        )
        return

    if message.contact.phone_number[0] != '+':
        contact_us.phone_number = '+' + message.contact.phone_number
    else:
        contact_us.phone_number = message.contact.phone_number
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot]['Toliq ism familiyangizni kiriting']
    )
    set_state(
        key=message.chat.id,
        value=States.SEND_NAME.value
    )


def check_name(name):
    for item in name:
        if item != ' ' and not item.isalpha():
            return False
    return True


@bot.message_handler(func=lambda message: get_state(message.chat.id) == States.SEND_NAME.value)
def send_name(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    if message.content_type != 'text' or not check_name(message.text):
        bot.send_message(
            chat_id=message.chat.id,
            text=dct[user.language_bot]['Iltimos Ism Familiyangizni Tog`ri kiriting!!!']
        )
        return

    contact_us.full_name = message.text
    markup = telebot.types.InlineKeyboardMarkup()
    courses = Course.objects.all()
    for course in courses:
        markup.row(telebot.types.InlineKeyboardButton(text=course.name, callback_data=course.name))
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot]["Qaysi kursga a'zo bo'lmoqchisiz?"],
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda call: True)
def cho_course(call):
    user, _ = get_user(call.from_user.id, call.from_user.username)
    contact_us.course = Course.objects.get(name=call.data)
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.id)
    bot.send_message(
        chat_id=call.from_user.id,
        text=dct[user.language_bot]['Arizangiz uchun rahmat, menedjerlarimiz siz bilan tez orada bog`lanishadi.']
    )
    contact_us.save()
    obj = ContactUs.objects.get(chat_id=contact_us.chat_id)
    bot.send_message(
        chat_id=manager_id,
        text='Name: ' + obj.full_name + '\n' + 'Phone number: ' + obj.phone_number + '\n' + 'Course: ' + str(
            obj.course.name) + '\n' + 'Date: ' + str(obj.date)[:20]
    )
    start_message(call.message)


@bot.message_handler(
    func=lambda message: message.text in ["⚙️Tilni o'zgartirish", "⚙️Изменить язык", "⚙️Change the language"])
def language_change(message):
    user, _ = get_user(message.chat.id, message.chat.username)
    markup = get_markup_change_language()
    bot.send_message(
        chat_id=message.chat.id,
        text=dct[user.language_bot]['🇺🇿Iltimos tilni tanlang'],
        reply_markup=markup,
    )


@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: get_state(key=message.chat.id) == States.START.value)
def start_message(message):
    set_state(
        key=message.chat.id,
        value=States.START.value
    )
    user, created = get_user(message.chat.id, message.chat.username)
    if created:
        markup = get_markup_change_language()
        bot.send_message(
            chat_id=message.chat.id,
            text='🇺🇿Iltimos tilni tanlang\n🇷🇺Пожалуйста выберите язык\n🇬🇧Please select a language',
            reply_markup=markup,
        )
        return
    else:
        markup = get_markup_menu(message.chat.id, message.chat.username)
        bot.send_message(
            chat_id=message.chat.id,
            text=dct[user.language_bot]['Menyu elementlaridan birini tanlang'],
            reply_markup=markup
        )
