from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

help_ = on_command('help', aliases={'帮助', 'searchbot'})


@help_.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await help_.send("""
命令起始符号：? ¿ / . 或（直接开始命令）

以下为命令列表：
  sou/搜/搜索/search/sch/?/？/¿ + 关键词
    获取关键词的搜索结果截图
        
  help/帮助/searchbot
    获取本段帮助""")
