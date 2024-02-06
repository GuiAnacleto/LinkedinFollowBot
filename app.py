import time
from app.bot.get_credentials import Credentials
from app.bot.linkedin import Linkedin

bot = Linkedin()
bot.loginLinkedin()
time.sleep(10)
bot.followPeople()
#emplementar modulo de enviar curriculo.
