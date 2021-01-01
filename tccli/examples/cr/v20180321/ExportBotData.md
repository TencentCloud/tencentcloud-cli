**Example 1: 查询机器人文件模板**



Input: 

```
tccli cr ExportBotData --cli-unfold-argument  \
    --Module AiApi \
    --Operation ExportBotData \
    --BizDate 2020-12-20 \
    --BotName 测试 \
    --BotId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx",
        "Data": [
            {
                "FileType": "A",
                "CosUrl": "https://aaa"
            }
        ]
    }
}
```

