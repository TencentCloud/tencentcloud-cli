**Example 1: AI 聊天问答**



Input: 

```
tccli es ChatCompletions --cli-unfold-argument  \
    --Messages.0.Role user \
    --Messages.0.Content 什么是大模型？ \
    --ModelName deepseek-r1 \
    --Stream False \
    --OnlineSearch True \
    --OnlineSearchOptions.Engine sogou
```

Output: 
```
{
    "Response": {
        "Id": "59afbba4-8b5f-47fa-972d-4bc5d77004ee",
        "Usage": {
            "PromptTokens": 9224,
            "CompletionTokens": 203,
            "TotalTokens": 9427
        },
        "Choices": [
            {
                "Message": {
                    "Role": "assistant",
                    "Content": "\n\n大模型是参数量庞大、基于深度学习的AI模型，擅长处理复杂任务如自然语言处理。",
                    "ReasoningContent": "\n嗯，用户让我简单描述什么是大模型，我需要先理解大模型的核心定义。根据搜索结果，大模型通常指参数规模庞大、基于深度学习的AI模型，比如GPT系列。多个网页提到参数数量达到数十亿甚至万亿，处理复杂任务能力强。例如，腾讯云和今日头条的文章都强调大模型的参数和数据处理能力。\n"
                }
            }
        ],
        "RequestId": "6b5a7f7a-3e3d-4974-8480-8e21edaec5e7",
        "OnlineSearchContent": [
            {
                "Query": "大模型 解释",
                "Title": "快速了解什么是大模型 - 今日头条",
                "Url": "https://m.toutiao.com/video/7340170115901932086/?upstream_biz=toutiao_pc",
                "Time": "2024-02-27",
                "Content": "大模型(Large Model)是AI人工智能领域中的一种重要模型,通常指的是参数量非常大、数据量也非常大的深度学习模型.大模型通常由数百万到数十亿的参数组成,需要大量的数据和计算资源进行训练和推理.",
                "ChunkIndex": "0",
                "Score": "0"
            }
        ]
    }
}
```

