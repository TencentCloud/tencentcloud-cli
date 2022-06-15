**Example 1: 日志列表**



Input: 

```
tccli dlc ListTaskJobLogDetail --cli-unfold-argument  \
    --TaskId xx \
    --StartTime 0 \
    --EndTime 0 \
    --Limit 0 \
    --Context xx
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

