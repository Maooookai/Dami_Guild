import random

import qqbot
from qqbot import MessageReference

from database.coin import coin_inquiry, add_coin
from database.dragon import dragon_get_coin, share_drop_coin_times, share_drop_coin_add


# 金币查询
def coin_have(message: qqbot.Message):
    return qqbot.MessageSendRequest(f"<@{message.author.id}>你有{coin_inquiry(message.author.id)}枚金币", message.id)


# 发言掉落金币次数查询
def check_get_coin(message: qqbot.Message) -> bool:
    if dragon_get_coin(message.author.id) >= 1:
        return False
    else:
        return True


# 好物分享获得金币
def share_get_coin(message: qqbot.Message):
    times = share_drop_coin_times(message.author.id)
    if 0 <= times < 3:
        share_drop_coin_add(message.author.id)
        qqbot.logger.info(f'{message.author.username}通过好物分享获得1金币')
        add_coin(message.author.id, 1, '好物分享')


# 随机获得金币
def random_add_coin(message: qqbot.Message):
    message_reference = MessageReference()
    message_reference.message_id = message.id
    salt = random.randint(1, 15)
    reason = '发言随机金币'
    if salt == 1:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"感觉你说的很有道理，送你{coin}金币！", message.id, message_reference=message_reference)
    elif salt == 2:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你这话真有意思，给你{coin}金币！", message.id, message_reference=message_reference)
    elif salt == 3:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"好，这是{coin}金币，请收下", message.id, message_reference=message_reference)
    elif salt == 4:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"笑死，给你{coin}金币", message.id, message_reference=message_reference)
    elif salt == 5:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"他真的，我哭死，给你{coin}金币", message.id, message_reference=message_reference)
    elif salt == 6:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"这都行? 给你{coin}金币", message.id, message_reference=message_reference)
    elif salt == 7:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"怎会如此，请收下{coin}金币", message.id, message_reference=message_reference)
    elif salt == 8:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"就这? 拿下这{coin}金币吧", message.id, message_reference=message_reference)
    elif salt == 9:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你真可爱! 我要给你{coin}金币!", message.id, message_reference=message_reference)
    elif salt == 10:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你看天上那朵云，像不像我现在送你的{coin}金币?", message.id, message_reference=message_reference)
    elif salt == 11:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"你好，请问你需要{coin}金币吗? 送你了！", message.id, message_reference=message_reference)
    elif salt == 12:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"哎呀，我突然多出了{coin}金币，给你了！", message.id, message_reference=message_reference)
    elif salt == 13:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"好棒哦，给你{coin}金币", message.id, message_reference=message_reference)
    elif salt == 14:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"我从Cyan那里偷来了{coin}个币，送你了，别跟他说哦！", message.id,
                                        message_reference=message_reference)
    elif salt == 15:
        coin = random.randint(1, 3)
        add_coin(message.author.id, coin, reason)
        return qqbot.MessageSendRequest(f"{message.author.username}！我好喜欢你啊！为了你,我要给你{coin}金币！", message.id,
                                        message_reference=message_reference)
