**Example 1: 日志列表**



Input: 

```
tccli dlc ListTaskJobLogDetail --cli-unfold-argument  \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --StartTime 0 \
    --Asc True \
    --Limit 0 \
    --Context xx \
    --TaskId xx \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ListOver": true,
        "Context": "xx",
        "Results": [
            {
                "Time": 1608794854001,
                "TopicId": "xxxx-xx-xx-xx-xxxxxxxx",
                "TopicName": "xxxxxxx",
                "LogJson": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            },
            {
                "Time": 1608794854001,
                "TopicId": "xxxx-xx-xx-xx-xxxxxxxx",
                "TopicName": "xxxxxxx",
                "LogJson": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            }
        ]
    }
}
```

