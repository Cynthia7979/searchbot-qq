from nonebot import on_command, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.adapters.cqhttp.exception import ActionFailed
from .search import get_img

# TODO: 添加图床简化图片上传逻辑

command_query = on_command('sou', aliases={'搜', '搜索', 'search', 'sch', '?', '？', '¿'})


@command_query.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message())
    print(f'[search_reply] msg: {msg}')
    keywords = msg.split()
    if keywords:
        try:
            filename = get_img(keywords)
            print(filename)
            seg = MessageSegment.image(filename)
            await command_query.send('以下是' + ', '.join(keywords) + '的搜索结果：')
            await command_query.send(seg)
            # await query.send(f"[CQ:image,file={filename}]")
        except ActionFailed:
            await command_query.send('发送失败。这种东西请自己去搜！')
    else:
        await command_query.send('？请输入查询词')
