from app.bot.get_credentials import Credentials
from app.bot.linkedin import Linkedin

bot = Linkedin()
bot.loginLinkedin()
bot.followPeople()