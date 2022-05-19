import datetime
import os

import pymysql
import qqbot
from qqbot.core.util.yaml_util import YamlUtil

config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
token = qqbot.Token(config["token"]["appid"], config["token"]["token"])
conn = pymysql.connect(
    host=config['mysql']['address'],
    port=config['mysql']['port'],
    user=config['mysql']['user'], password=config['mysql']['password'],
    database=config['mysql']['database'],
    charset='utf8')


# 增加一次发言记录
def add_dragon_once(user_id: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_add_speak = f"""
    update dragon set speak_count=speak_count+1 where user_id='{user_id}'and date='{current_date}';
    """
    cursor.execute(sql_add_speak)
    conn.commit()
    cursor.close()


# 检查今日是否已创建
def check_dragon_exists(user_id: str) -> bool:
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_check_user = f"""
    select * from dragon where user_id='{user_id}'and date='{current_date}';
    """
    cursor.execute(sql_check_user)
    conn.commit()
    if len(cursor.fetchall()) != 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False


# 创建今日统计
def add_dragon_today(user_id: str):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    sql_add_today = f"""
    insert into dragon(user_id, speak_count, date, get_coin, share_coin) values ('{user_id}',1,'{current_date}',0,0);
    """
    cursor.execute(sql_add_today)
    conn.commit()
    cursor.close()


# 查询发言排行
def dragon_top():
    conn.ping(reconnect=True)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor = conn.cursor()
    sql_dragon_top = f"""
    select user_id,speak_count from dragon where date='{current_date}' order by speak_count desc limit 10;
    """
    cursor.execute(sql_dragon_top)
    conn.commit()
    result = cursor.fetchall()
    cursor.close()
    return result


# 查询发言掉落金币次数
def dragon_get_coin(user_id: str):
    conn.ping(reconnect=True)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor = conn.cursor()
    sql_get_coin = f"""
    select get_coin from dragon where date='{current_date}' and user_id='{user_id}';
    """
    cursor.execute(sql_get_coin)
    conn.commit()
    result = cursor.fetchall()[0][0]
    cursor.close()
    return result


# 增加发言掉落金币次数
def dragon_get_coin_add(user_id: str):
    conn.ping(reconnect=True)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor = conn.cursor()
    sql_get_coin = f"""
    update dragon set get_coin=get_coin+1 where user_id='{user_id}' and date='{current_date}';
    """
    cursor.execute(sql_get_coin)
    conn.commit()
    cursor.close()


# 查询昨日龙王
def dragon_top_yesterday():
    conn.ping(reconnect=True)
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    cursor = conn.cursor()
    sql_dragon_top = f"""
    select user_id,speak_count from dragon where date='{yesterday}' order by speak_count desc limit 1;
    """
    cursor.execute(sql_dragon_top)
    conn.commit()
    result = cursor.fetchall()
    cursor.close()
    return result


# 查询好物分享掉落金币次数
def share_drop_coin_times(user_id: str):
    conn.ping(reconnect=True)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor = conn.cursor()
    sql_check_share_coin = f"""
    select share_coin from dragon where user_id='{user_id}' and date='{current_date}';
    """
    cursor.execute(sql_check_share_coin)
    conn.commit()
    result = cursor.fetchall()
    cursor.close()
    return int(result[0][0])


# 增加好物分享掉落金币次数
def share_drop_coin_add(user_id: str):
    conn.ping(reconnect=True)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor = conn.cursor()
    sql_get_coin = f"""
    update dragon set share_coin=share_coin+1 where user_id='{user_id}' and date='{current_date}';
    """
    cursor.execute(sql_get_coin)
    conn.commit()
    cursor.close()
