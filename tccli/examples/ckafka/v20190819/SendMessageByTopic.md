**Example 1: 发送消息**

发送消息

Input: 

```
tccli ckafka SendMessageByTopic --cli-unfold-argument  \
    --InstanceId abc \
    --TopicName abc \
    --Message abc \
    --Key abc \
    --Partition 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "abc",
            "ReturnMessage": "abc",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "abc"
    }
}
```

