**Example 1: 发布文档预览**



Input: 

```
tccli lke ListReleaseDocPreview --cli-unfold-argument  \
    --BotBizId 1798610639288008723 \
    --Query  \
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
        "Total": "1",
        "List": [
            {
                "FileName": "test.txt",
                "FileType": "test.txt",
                "UpdateTime": "1701766219",
                "Action": 1,
                "ActionDesc": "新增",
                "Message": ""
            }
        ],
        "RequestId": "2314bdbe-da7e-401e-95c4-3e861d5298ee"
    }
}
```

