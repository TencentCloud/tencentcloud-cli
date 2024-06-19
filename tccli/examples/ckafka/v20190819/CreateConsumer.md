**Example 1: 创建消费者**

创建消费者

Input: 

```
tccli ckafka CreateConsumer --cli-unfold-argument  \
    --InstanceId ckafka-xxx \
    --TopicName topic-xxx \
    --GroupName group-xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnMessage": "abc",
            "ReturnCode": "abc",
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

