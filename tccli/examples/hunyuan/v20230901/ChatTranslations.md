**Example 1: 非流式调用翻译接口**

非流式调用翻译接口

Input: 

```
tccli hunyuan ChatTranslations --cli-unfold-argument  \
    --Model hunyuan-translation \
    --Stream False \
    --Text Playing video games leads to lasting improvements in cognitive abilities. \
    --Source en \
    --Target zh \
    --Field 游戏剧情 \
    --References.0.Type sentence \
    --References.0.Text Computer games are a perfect recipe for strengthening our cognitive skills \
    --References.0.Translation 电脑游戏是增强我们认知能力的完美秘诀
```

Output: 
```
{
    "Response": {
        "RequestId": "e638f0a0-a2a5-4c43-a1c6-798a7cbfbb18",
        "Id": "e638f0a0-a2a5-4c43-a1c6-798a7cbfbb18",
        "Created": 1733133524,
        "Choices": [
            {
                "Index": 0,
                "Message": {
                    "Role": "assistant",
                    "Content": "玩视频游戏会导致认知能力持久的提升。"
                },
                "FinishReason": "stop"
            }
        ],
        "Usage": {
            "PromptTokens": 96,
            "CompletionTokens": 10,
            "TotalTokens": 106
        },
        "Note": "以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记"
    }
}
```

