from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.ext import Dispatcher, ConversationHandler
from methods.base import start, get_language, get_phonenumber, phone_number_error, error_message, get_offer, \
    get_application_type, \
    get_company_name, get_company_inn, get_business_center, get_business_type
from states import State as st
from decouple import config

TOKEN = config('TOKEN')

update = Updater(token=TOKEN, use_context=True, workers=1000)

dispatcher: Dispatcher = update.dispatcher

hand_command = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        st.LANGUAGE: [
            CommandHandler('start', start),
            CallbackQueryHandler(get_language),
            MessageHandler(Filters.all, error_message)
        ],
        st.PHONE: [
            CommandHandler('start', start),
            MessageHandler(Filters.contact & Filters.forwarded, phone_number_error),
            MessageHandler(Filters.contact, get_phonenumber),
            MessageHandler(Filters.text & Filters.forwarded, phone_number_error)
        ],
        st.OFFER: [
            CommandHandler('start', start),
            MessageHandler(Filters.text, get_offer)
        ],
        st.APPLICATION_TYPE: [
            CommandHandler('start', start),
            CallbackQueryHandler(get_application_type),
            # MessageHandler(Filters.text, get_application_type)
        ],
        st.COMPANY_NAME: [
            CommandHandler('start', start),
            MessageHandler(Filters.text, get_company_name)
        ],
        st.COMPANY_INN: [
            CommandHandler('start', start),
            MessageHandler(Filters.text, get_company_inn)
        ],
        st.BISENESS_CENTER: [
            CommandHandler('start', start),
            CallbackQueryHandler(get_business_center),
        ],
        st.BISENESS_TYPE: [
            CommandHandler('start', start),
            CallbackQueryHandler(get_business_type),
        ],
        st.BASE: [
            CommandHandler('start', start),
            MessageHandler(Filters.all, error_message)
        ]
    },
    fallbacks=[MessageHandler(Filters.all, error_message)],
    run_async=True
)

dispatcher.add_handler(handler=hand_command)
update.start_polling()
print('started polling')
update.idle()
