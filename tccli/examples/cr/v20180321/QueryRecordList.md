**Example 1: 查询录音列表**



Input: 

```
tccli cr QueryRecordList --cli-unfold-argument  \
    --EndBizDate 2020-09-22 \
    --CalledPhone xx \
    --BotId xx \
    --Module xx \
    --Limit 0 \
    --Offset 0 \
    --Operation xx \
    --StartBizDate 2020-09-22 \
    --BotName xx
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "CallStartTime": "2020-09-22 00:00:00",
                "DialogueLog": "xx",
                "CalledPhone": "xx",
                "BotId": "xx",
                "BizDate": "2020-09-22",
                "Duration": 0,
                "CosUrl": "xx",
                "BotName": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalCount": 0
    }
}
```

