# 大米频道版
## 介绍  
群聊娱乐机器人，可以进行一些简单的交互以及游戏  
## 已实现的功能  
### 指令  
#### 图片查询  
使用[百度随机图片搜索接口](https://github.com/Maooookai/BaiduImageSearchAPI)返回一张随机相关图片  
具体用法为：`@机器人 /图片 红茶`  
#### 英语每日一句查询  
使用[金山词霸每日一句接口](https://open.iciba.com/dsapi/)返回每日一句信息  
具体用法为：`@机器人 /每日一句`  
#### 金币查询  
查询当前持有的金币  
具体用法为：`@机器人 /查询`  
#### 每日打卡  
获得随机1-3金币，一天一次  
具体用法为：`@机器人 /打卡`  
#### 每日乞讨  
获得随机0-5金币，一天一次，与打卡共享次数  
具体用法为：`@机器人 /乞讨`  
#### 召唤  
花费5金币从数据库中随机获得一张卡，不同星级对应不同积分  
具体用法为：`@机器人 /召唤`  
#### 召唤查询  
查询已经抽到的卡  
具体用法为：`@机器人 /抽卡查询`  
#### 排行榜  
查询抽卡积分排行榜  
具体用法为：`@机器人 /排行榜`  
#### 水群  
查询发言次数排行榜  
具体用法为：`@机器人 /水群`  
### 被动消息  
#### 疯狂星期四  
当接收到消息时，如果今天是星期四，则有概率随机发送一条疯狂星期四文案  
#### 人工智障  
当接收到消息时，如果内容以“吗结尾”，则有概率去掉“吗”并加上感叹号发送出去  
## 更多待补充...