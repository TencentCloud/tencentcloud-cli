**Example 1: 设置主题属性**



Input: 

```
tccli ckafka ModifyTopicAttributes --cli-unfold-argument  \
    --InstanceId xxx \
    --Note xxx \
    --TopicName xxx
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

