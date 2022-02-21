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
            "ReturnMessage": "xx",
            "ReturnCode": "xx",
            "Data": {
                "FlowId": 0
            }
        },
        "RequestId": "xx"
    }
}
```

