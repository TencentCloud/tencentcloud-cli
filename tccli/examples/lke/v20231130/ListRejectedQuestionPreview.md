**Example 1: 发布拒答问题预览**



Input: 

```
tccli lke ListRejectedQuestionPreview --cli-unfold-argument  \
    --BotBizId 1798610639288008723 \
    --PageNumber 1 \
    --PageSize 1 \
    --Query  \
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
                "UpdateTime": "1701766284",
                "Action": 1,
                "ActionDesc": "新增",
                "Message": ""
            }
        ],
        "RequestId": "2314bdbe-d34e-401e-95c4-3e861d5298ee"
    }
}
```

