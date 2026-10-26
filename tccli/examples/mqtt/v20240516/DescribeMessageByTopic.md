**Example 1: 示例**



Input: 

```
tccli mqtt DescribeMessageByTopic --cli-unfold-argument  \
    --InstanceId mqtt-mwe5jvvr \
    --Topic home/room/1 \
    --StartTime 1776739183514 \
    --MaxNumber 1024 \
    --FilterExpression LmxldmVsID09ICJFUlJPUiI=
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ClientId": "client-1",
                "MessageId": "155A50E000486587524C6954F59CD00C",
                "OriginTopic": "home/room/1",
                "Qos": "1",
                "StoreTimestamp": 1776739975581
            }
        ],
        "RequestId": "795c52c7-ff55-4cb4-8371-387789a41265"
    }
}
```

