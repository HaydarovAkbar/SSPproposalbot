from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from .texts import KeyboardsText as kbt
from integration.base import IntegrationSSP as ssp


class Button:
    @staticmethod
    def language():
        msg = kbt.language
        # button = ReplyKeyboardMarkup([
        #     [msg[0]],
        #     [msg[1]],
        #     [msg[2]],
        # ], resize_keyboard=True)
        button = InlineKeyboardMarkup([
            [InlineKeyboardButton(msg[0], callback_data='uz_latn')],
            [InlineKeyboardButton(msg[1], callback_data='uz_cyrl')],
            [InlineKeyboardButton(msg[2], callback_data='ru')],
        ])
        return button

    @staticmethod
    def phone_batton(lang='uz_latn'):
        text = kbt.phone_number.get(lang)
        phone = KeyboardButton(text, request_contact=True)
        contact_key = ReplyKeyboardMarkup([[phone]], resize_keyboard=True)
        return contact_key

    @staticmethod
    def back(lang='uz_latn'):
        bt_txt = kbt.back.get(lang)
        batton = ReplyKeyboardMarkup([
            [bt_txt],
        ], resize_keyboard=True)
        return batton

    @staticmethod
    def application_type(lang='uz_latn'):
        ssp_application = ssp.get_all_application_type(lang)
        button, bt_txt = [], []
        for app in ssp_application:
            bt_txt.append(InlineKeyboardButton(app['text'], callback_data=app['value']))
            button.append(bt_txt)
            bt_txt = []
        return InlineKeyboardMarkup(button)

    @staticmethod
    def business_sector(lang='uz_latn'):
        ssp_business = ssp.business_sector_list(lang)
        button, bt_txt = [], []
        for app in ssp_business:
            bt_txt.append(InlineKeyboardButton(app['text'], callback_data=app['value']))
            button.append(bt_txt)
            bt_txt = []
        return InlineKeyboardMarkup(button)

    @staticmethod
    def proposal_subject(lang='uz_latn', page=1):
        ssp_subject = ssp.proposal_subject_list(lang)
        button, bt_txt = [], []
        count = len(ssp_subject)
        end_limit = page * 10
        start_limit = end_limit - 10
        result_text = {
            'uz_latn': f"Natijalar {start_limit + 1}-{end_limit}:   {count} dan\n\n",
            'uz_cyrl': f"Натижалар {start_limit + 1}-{end_limit}:   {count} дан\n\n",
            'ru': f"Результаты {start_limit + 1}-{end_limit}:   {count} из\n\n",
        }.get(lang)
        counter = 1
        for app in ssp_subject[start_limit:end_limit]:
            result_text += f"{counter}. {app['text']}\n"
            if len(bt_txt) < 5:
                bt_txt.append(InlineKeyboardButton(f"{counter}", callback_data=f"{app['value']}"))
            else:
                button.append(bt_txt)
                bt_txt = [InlineKeyboardButton(f"{counter}", callback_data=f"{app['value']}")]
            counter += 1
        button.append(bt_txt)
        button.append([InlineKeyboardButton(f"⬅️", callback_data="left"),
                       # InlineKeyboardButton(f"️❌", callback_data="delete"),
                       InlineKeyboardButton(f"️➡", callback_data="right")])
        return InlineKeyboardMarkup(button), result_text

    @staticmethod
    def get_company_type(lang='uz_latn'):
        ssp_company_type = ssp.get_company_type_list(lang)
        button, bt_txt = [], []
        for app in ssp_company_type:
            bt_txt.append(InlineKeyboardButton(app['text'], callback_data=app['value']))
            button.append(bt_txt)
            bt_txt = []
        return InlineKeyboardMarkup(button)
