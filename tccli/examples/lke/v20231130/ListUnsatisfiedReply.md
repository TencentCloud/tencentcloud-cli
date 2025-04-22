**Example 1: 查询不满意回复列表**

查询不满意回复列表

Input: 

```
tccli lke ListUnsatisfiedReply --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --PageNumber 1 \
    --PageSize 15 \
    --Query 你好 \
    --Reasons 其他价值观问题
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Answer": "对话主题：无",
                "Question": "你好吗",
                "Reasons": [
                    "存在逻辑问题",
                    "存在偏见与歧视"
                ],
                "RecordBizId": "YWm_20241206_155222_578_Xg6FvVzX",
                "ReplyBizId": "1864940953108241344"
            }
        ],
        "RequestId": "a94afdd8-decb-487a-a37a-4c053654385b",
        "Total": "1"
    }
}
```

