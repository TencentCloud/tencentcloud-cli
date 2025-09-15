**Example 1: 发送消息**

发送消息

Input: 

```
tccli ckafka SendMessageByTopic --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --TopicName topic-test \
    --Message message-test \
    --Key key-test \
    --Partition 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "success",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "d173b4fb-c6d0-4507-a822-b6f277fc4016"
    }
}
```

