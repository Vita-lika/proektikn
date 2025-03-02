from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


TOKEN = '7860416169:AAGF5b6qr42qQeBn34mesIGIZYwQBqF5AzM'


tasks = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я твой персональный планировщик дня.')

def add_task(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    task = update.message.text.split(maxsplit=1)[1]
    if user_id not in tasks:
        tasks[user_id] = []
    tasks[user_id].append(task)
    update.message.reply_text(f'Задача "{task}" добавлена!')

def list_tasks(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in tasks and len(tasks[user_id]) > 0:
        message = '\n'.join([f'{i+1}. {t}' for i, t in enumerate(tasks[user_id])])
        update.message.reply_text(f'Твои задачи:\n{message}')
    else:
        update.message.reply_text('У тебя нет активных задач.')

def clear_tasks(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in tasks:
        del tasks[user_id]
        update.message.reply_text('Все задачи удалены.')
    else:
        update.message.reply_text('Нечего удалять — у тебя нет активных задач.')

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Извини, я не понял эту команду.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('add', add_task))
    dispatcher.add_handler(CommandHandler('list', list_tasks))
    dispatcher.add_handler(CommandHandler('clear', clear_tasks))
    

    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

  
    updater.start_polling()
    print('Бот запущен...')
    updater.idle()

if __name__ == '__main__':
    main()
