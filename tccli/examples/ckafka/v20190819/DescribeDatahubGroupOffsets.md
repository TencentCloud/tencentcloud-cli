**Example 1: 获取消费分组offset**



Input: 

```
tccli ckafka DescribeDatahubGroupOffsets --cli-unfold-argument  \
    --Group "group" \
    --Name name
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "TopicList": [
                {
                    "Topic": "topic-test",
                    "Partitions": [
                        {
                            "Partition": 0,
                            "Offset": 22689638,
                            "Metadata": "",
                            "ErrorCode": 0,
                            "LogEndOffset": 207927929,
                            "Lag": 185238291
                        }
                    ]
                }
            ]
        },
        "RequestId": "fd9afa97-cc0f-4ea7-9da8-63914a0877e1"
    }
}
```

