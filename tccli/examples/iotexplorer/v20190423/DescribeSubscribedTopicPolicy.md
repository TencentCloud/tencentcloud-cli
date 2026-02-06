**Example 1: 获取设备已订阅Topic列表**



Input: 

```
tccli iotexplorer DescribeSubscribedTopicPolicy --cli-unfold-argument  \
    --ProductId TRTC3ZCK4P \
    --DeviceName dev002
```

Output: 
```
{
    "Response": {
        "RequestId": "request-id",
        "Topics": [
            {
                "TopicName": "$thing/down/property/TRTC3ZCK4P/dev002"
            },
            {
                "TopicName": "$video/down/service/TRTC3ZCK4P/dev002"
            }
        ]
    }
}
```

