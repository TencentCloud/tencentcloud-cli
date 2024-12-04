**Example 1: 创建消费者**

创建消费者

Input: 

```
tccli ckafka CreateConsumer --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --TopicName topic-test \
    --GroupName group-test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnMessage": "success",
            "ReturnCode": "ok",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "9e6d209b-69fd-4a00-b064-75131aa0a0f8"
    }
}
```

