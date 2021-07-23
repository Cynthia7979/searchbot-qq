# SearchBot

基于Nonebot和go-cqhttp实现的QQ搜索机器人

本repo包含：
* 必要插件
* bot.py
* 环境文件

要使用SearchBot，还需额外配置：
* `go-cqhttp`：参考[CQHTTP协议](https://v2.nonebot.dev/guide/cqhttp-guide.html)
* 运行环境：参考[安装](https://v2.nonebot.dev/guide/installation.html)
* 修改`src/plugins/search-reply/search.py`中的路径配置