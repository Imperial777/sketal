import datetime
import calendar
from plugin_system import Plugin

plugin = Plugin('Недели')

answers = {}
answers[True] = "Неделя чётная"
answers[False] = "Неделя нечётная (верхняя)."


@plugin.on_command('неделя', 'какая неделя')
def get_weeks(vk, msg, args):
    #  получить время по МСК (UTC +3)
    time = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3))
    week_number = (time.day - 1) // 7 + 2
    is_even = week_number % 2 == 0
    vk.respond(msg, {'message': 'Сейчас {number} неделя в месяце.\n'.format(number=week_number) + answers[is_even]})