from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def main():
    TECH_VJ_BOT_TOKEN = os.environ.get("TECH_VJ_BOT_TOKEN", "8108185474:AAHhUu6H9BeEp0ZHN46V_sjvK2FtViwMUYk")
    TECH_VJ_BOT_USERNAME = os.environ.get("TECH_VJ_BOT_USERNAME", "uploader_yang_bot") # Bot username without @
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # បន្ថែម Douyin Handler ជាឧទាហរណ៍ក្នុង Command /douyin
    dp.add_handler(CommandHandler("douyin", douyin_handler))
    
    # ឬបន្ថែម MessageHandler ពិនិត្យករណី URL (បើអ្នកចង់អោយ Bot ត្រួតពិនិត្យ URL នៅក្នុង message ទាំងអស់)
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, douyin_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
