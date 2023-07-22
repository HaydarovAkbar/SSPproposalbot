from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from keyboards.base import Button as base_button
from dictionary.base import MessageText as msg
from states import State as st
from keyboards.texts import KeyboardsText as kbt
from integration.base import IntegrationSSP as ssp


def start(update: Update, context: CallbackContext):
    lang = update.effective_user.language_code
    update.message.reply_html(text=msg.base.get(lang).format(update.effective_user.full_name),
                              reply_markup=base_button.language())
    return st.LANGUAGE


def get_language(update: Update, context: CallbackContext):
    query = update.callback_query
    lang = query.data
    context.user_data['lang'] = lang
    query.delete_message(timeout=1)
    context.bot.send_message(chat_id=update.effective_user.id, text=msg.get_phone_number.get(lang), parse_mode="HTML",
                             reply_markup=base_button.phone_batton(lang))
    return st.PHONE


def phone_number_error(update: Update, context: CallbackContext):
    update.message.reply_html(text=msg.phone_number_error, reply_markup=base_button.phone_batton())
    return st.PHONE


def get_phonenumber(update: Update, context: CallbackContext):
    phone = update.message.contact.phone_number
    lang = context.user_data['lang']
    context.user_data['phone'] = phone
    a = update.message.reply_html(text=msg.enter_phone_number.get(lang), reply_markup=ReplyKeyboardRemove())
    context.bot.send_message(
        chat_id=update.effective_user.id,
        text=msg.application_type.get(lang),
        reply_markup=base_button.application_type(lang)
    )
    context.bot.delete_message(chat_id=update.effective_user.id, message_id=a.message_id, timeout=2)
    return st.APPLICATION_TYPE


def get_offer(update: Update, context: CallbackContext):
    lang = context.user_data['lang']
    context.user_data['fullname'] = update.effective_user.full_name
    create = ssp.create_proposal(data=context.user_data)
    if create == 200:
        update.message.reply_html(text=msg.successfully.get(lang))
        return st.BASE
    update.message.reply_text(
        text=msg.error_message.get(lang),
        reply_markup=ReplyKeyboardRemove()
    )
    return st.BASE


def error_message(update: Update, context: CallbackContext):
    lang = context.user_data['lang'] if 'lang' in context.user_data else 'uz_cyrl'
    update.message.reply_html(text=msg._error_message.get(lang), reply_markup=ReplyKeyboardRemove())
    return st.LANGUAGE


def get_application_type(update: Update, context: CallbackContext):
    query = update.callback_query
    application_type = query.data
    lang = context.user_data['lang']
    context.user_data['application_type'] = application_type
    if query.data == '1':
        query.edit_message_text(text=msg.enter_company_name.get(lang))
        return st.COMPANY_NAME
    query.edit_message_text(text=msg.business_sector.get(lang), reply_markup=base_button.business_sector(lang))
    return st.BISENESS_CENTER


def get_company_name(update: Update, context: CallbackContext):
    company_name = update.message.text
    lang = context.user_data['lang']
    context.user_data['company_name'] = company_name
    update.message.reply_html(text=msg.enter_company_inn.get(lang))
    return st.COMPANY_INN


def get_company_inn(update: Update, context: CallbackContext):
    company_inn = update.message.text
    lang = context.user_data['lang']
    if not company_inn.isdigit() or len(company_inn) != 9:
        update.message.reply_html(text=msg.enter_company_inn.get(lang))
        return st.COMPANY_INN
    context.user_data['company_inn'] = company_inn
    update.message.reply_html(text=msg.business_sector.get(lang),
                              reply_markup=base_button.business_sector(lang))
    return st.BISENESS_CENTER


def get_business_center(update: Update, context: CallbackContext):
    query = update.callback_query
    lang = context.user_data['lang']
    context.user_data['business_center'] = query.data
    page = 1
    button, text = base_button.proposal_subject(lang, page)
    context.user_data['page'] = page
    query.edit_message_text(text=text,
                            reply_markup=button)
    return st.BISENESS_TYPE


def get_business_type(update: Update, context: CallbackContext):
    query = update.callback_query
    lang = context.user_data['lang']
    page = context.user_data.get('page', 0)
    if query.data == 'delete':
        query.delete_message()
        return st.BISENESS_CENTER
    elif query.data == 'right':
        page += 1
        if page > 8:
            query.answer(text=msg.last_page.get(lang))
            return st.BISENESS_TYPE
    elif query.data == 'left':
        page -= 1
        if page < 1:
            query.answer(text=msg.last_page.get(lang))
            return st.BISENESS_TYPE
    else:
        context.user_data['business_type'] = query.data
        query.delete_message()
        context.bot.send_message(chat_id=update.effective_user.id,text=msg.get_offer.get(lang))
        return st.OFFER
    context.user_data['page'] = page
    button, text = base_button.proposal_subject(lang, page)
    query.edit_message_text(text=text,
                            reply_markup=button)
    return st.BISENESS_TYPE
