**Example 1: 发布拒答问题预览**



Input: 

```
tccli lke ListRejectedQuestionPreview --cli-unfold-argument  \
    --BotBizId abc \
    --PageNumber 1 \
    --PageSize 1 \
    --Query abc \
    --ReleaseBizId 1 \
    --Actions 1 \
    --StartTime 1701566284 \
    --EndTime 1701766284
```

Output: 
```
{
    "Response": {
        "Total": "1",
        "List": [
            {
                "Question": "abc",
                "UpdateTime": "abc",
                "Action": 1,
                "ActionDesc": "abc",
                "Message": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

