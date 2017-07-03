#coding:utf-8

import slackbot.bot
import random

@slackbot.bot.respond_to(r'^dice\s+(\d+)')
def resp_fizzbuz(message,digitstr):
    num1 = int(digitstr)
    if 1 <= num1 <= 30:
        i = 1
        avgsum = 0.0
        count = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
        while i <= num1:
            roll = random.randint(1,6)
            count[str(roll)] += 1
            message.reply(str(i) + '回目のサイコロ ' + str(roll))
            avgsum += roll
            i += 1
        mode = 1
        j = 1
        while j <= 5:
            if count[str(j)] < count[str(j + 1)]:
                mode = j + 1
            #elif count[str(j)] == count[str(j + 1)]:
                #mode1 = j + 1
            j += 1
        avg = avgsum / num1
        message.reply('平均値は' + str(avg))
        message.reply('最頻値は' + str(mode) + "(" + str(count[str(mode)]) + "回登場)")
