class MessageText:
    base = {
        'uz_latn': "Assalomu alaykum, {}!\n\nTilni tanlang:",
        'uz_cyrl': "Ассалому алайкум, {}!\n\nТилни танланг:",
        'ru': "Здравствуйте, {}!\n\nВыберите язык:",
        'en': "Hello, {}!\n\nChoose a language:"
    }
    get_phone_number = {
        'uz_latn': "<b>Telefon nomeringizni kiriting:</b>",
        'uz_cyrl': "<b>Телефон номерингизни киритинг:</b>",
        'ru': "<b>Введите номер телефона:</b>",
        'en': "Enter your phone number:"
    }

    phone_number_error = {
        'uz_latn': "Telefon nomeringizni noto'g'ri kiritdingiz. Iltimos, qaytadan urinib ko'ring:",
        'uz_cyrl': "Телефон номерингизни нотўғри киритдингиз. Илтимос, қайтадан уриниб кўринг:",
        'ru': "Вы ввели неправильный номер телефона. Пожалуйста, попробуйте еще раз:",
        'en': "You entered the wrong phone number. Please try again:"
    }

    get_offer = {
        'uz_latn': "Taklifingizni kiriting:",
        'uz_cyrl': "Таклифингизни киритинг:",
        'ru': "Введите предложение:",
        'en': "Enter your suggestion:"
    }

    get_appeal = {
        'uz_latn': "Murojaatingizni kiriting:",
        'uz_cyrl': "Мурожаатингизни киритинг:",
        'ru': "Введите обращение:",
        'en': "Enter your appeal:"
    }

    successfully = {
        'uz_latn': "<code>Taklifingiz muvaffaqiyatli yuborildi! </code>✅\n\n<b>Yana taklif yuborish uchun /start buyrug'ini yuboring.</b>",
        'uz_cyrl': "<code>Таклифингиз муваффақиятли юборилди!</code> ✅\n\n<b>Яна таклиф юбориш учун /start буюрғини юборинг.</b>",
        'ru': "<code>Ваше предложение успешно отправлено!</code> ✅\n\n<b>Для отправки еще одного предложения отправьте команду /start.</b>",
        'en': "Your suggestion has been successfully sent!\n\n<b>To send another suggestion, send the /start command.</b>"
    }

    error_message = {
        'uz_latn': "<b>Murojaatingiz yuborilmadi!</b>\n\nIltimos, qaytadan urinib ko'ring./start buyrug'ini yuboring.",
        'uz_cyrl': "<b>Мурожаатингиз юборилмади!</b>\n\nИлтимос, қайтадан уриниб кўринг. /start буюрғини юборинг.",
        'ru': "<b>Ваша заявка не отправлена!</b>\n\nПожалуйста, попробуйте еще раз. Отправьте команду /start.",
        'en': "<b>Your application has not been sent!</b>\n\nPlease try again."
    }

    tg_error_message = {
        'uz_latn': "<code>Xato xabar kiritdingiz.</code>\n\n/start buyrug'ini yuboring.",
        'uz_cyrl': "<code>Хато хабар киритдингиз.</code>\n\n/start буюрғини юборинг.",
        'ru': "<code>Вы ввели неправильное сообщение.</code>\n\nОтправьте команду /start.",
        'en': "<code>An error occurred! Please try again.</code>"
    }

    application_type = {
        'uz_latn': "Murojaatchi turini tanlang:",
        'uz_cyrl': "Мурожаатчи турини танланг:",
        'ru': "Выберите тип заявителя:",
        'en': "Choose the type of applicant:"
    }

    business_sector = {
        'uz_latn': "Tadbirkorlik sohasini tanlang:",
        'uz_cyrl': "Тадбиркорлик соҳасини танланг:",
        'ru': "Выберите сферу предпринимательства:",
        'en': "Choose a business sector:"
    }

    enter_company_name = {
        'uz_latn': "Korxonaning nomini kiriting:",
        'uz_cyrl': "Корхонанинг номини киритинг:",
        'ru': "Введите название компании:",
    }

    error_company_name = {
        'uz_latn': "Korxonaning nomini noto'g'ri kiritdingiz. Iltimos, qaytadan urinib ko'ring:",
        'uz_cyrl': "Корхонанинг номини нотўғри киритдингиз. Илтимос, қайтадан уриниб кўринг:",
        'ru': "Вы ввели название компании неправильно. Пожалуйста, попробуйте еще раз:",
    }

    enter_company_inn = {
        'uz_latn': "Korxonaning INN raqamini kiriting:",
        'uz_cyrl': "Корхонанинг ИНН рақамини киритинг:",
        'ru': "Введите ИНН компании:",
    }

    error_company_inn = {
        'uz_latn': "Korxonaning INN raqamini noto'g'ri kiritdingiz. Iltimos, qaytadan urinib ko'ring:",
        'uz_cyrl': "Корхонанинг ИНН рақамини нотўғри киритдингиз. Илтимос, қайтадан уриниб кўринг:",
        'ru': "Вы ввели ИНН компании неправильно. Пожалуйста, попробуйте еще раз:",
    }

    subject_of_application = {
        'uz_latn': "Murojaat mavzusini tanlang:",
        'uz_cyrl': "Мурожаат мавзусини танланг:",
        'ru': "Выберите тему обращения:",
    }

    enter_phone_number = {
        'uz_latn': "Telefon raqamingiz kiritildi.",
        'uz_cyrl': "Телефон рақамингиз киритилди.",
        'ru': "Ваш номер телефона был введен.",
    }

    last_page = {
        'uz_latn': "Bu oxirgi sahifa edi",
        'uz_cyrl': "Бу охирги саҳифа эди",
        'ru': "Это была последняя страница",
    }

    vote = {
        'uz_latn': """
Oʼzbekiston Savdo-sanoat palatasi tomonidan tadbirkorlik faoliyatini oʼrganish, biznes yuritishda duch kelinayotgan tizimli muammolarni aniqlash maqsadida soʼrovnoma oʼtkazilmoqda. 

Quyidagi havola orqali soʼrovnomani toʼldirishingiz mumkin: https://ee.humanitarianresponse.info/QvDmcMon

Mamlakatimiz ishbilarmonlik muhitini rivojlantirishda faol ishtirok eting!
""",
        'uz_cyrl': """
Ўзбекистон Савдо-саноат палатаси томонидан тадбиркорлик фаолиятини ўрганиш, бизнес юритишда дуч келинайотган тизимли муаммоларни аниқлаш мақсадида сўровнома ўтказилмоқда. 

Қуйидаги ҳавола орқали сўровномани тўлдиришингиз мумкин: https://ee.humanitarianresponse.info/QvDmcMon

Мамлакатимиз ишбилармонлик муҳитини ривожлантиришда фаол иштирок этинг!
""",
        'ru': """
Торгово-промышленная палата Узбекистана проводит опрос с целью выявления системных проблем, с которыми сталкиваются предприниматели в процессе осуществления предпринимательской деятельности.

Опрос можно заполнить по следующей ссылке: https://ee.humanitarianresponse.info/QvDmcMon

Принимайте активное участие в развитии предпринимательской среды в нашей стране!
""",
    }

    choose_value = {
        'uz_latn': "Siz <code>{}</code> tanladingiz!",
        'uz_cyrl': "Сиз <code>{}</code> танладингиз!",
        'ru': "Вы выбрали <code>{}</code>!",
    }

    enter_company_type = {
        'uz_latn': "Tashkilot turini kiriting:",
        'uz_cyrl': "Ташкилот турини киритинг:",
        'ru': "Введите тип организации:",
    }