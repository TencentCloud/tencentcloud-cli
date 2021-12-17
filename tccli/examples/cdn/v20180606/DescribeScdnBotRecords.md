**Example 1: 获取指定类型的BOT记录**



Input: 

```
tccli cdn DescribeScdnBotRecords --cli-unfold-argument  \
    --BotType TCB \
    --Domain 123.com \
    --StartTime '2020-04-20 12:00:00' \
    --EndTime '2020-04-20 23:59:59' \
    --Offset 0 \
    --Limit 20 \
    --SortBy.0.Key timestamp \
    --SortBy.0.Sequence desc \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [],
        "RequestId": "6d04373b-ba59-4a4f-a96e-9fe53b59a536"
    }
}
```

