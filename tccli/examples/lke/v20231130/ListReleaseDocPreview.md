**Example 1: 发布文档预览**



Input: 

```
tccli lke ListReleaseDocPreview --cli-unfold-argument  \
    --BotBizId abc \
    --Query abc \
    --ReleaseBizId 1 \
    --PageNumber 1 \
    --PageSize 1 \
    --StartTime 1701566219 \
    --EndTime 1701766219 \
    --Actions 1
```

Output: 
```
{
    "Response": {
        "Total": "abc",
        "List": [
            {
                "FileName": "abc",
                "FileType": "abc",
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

