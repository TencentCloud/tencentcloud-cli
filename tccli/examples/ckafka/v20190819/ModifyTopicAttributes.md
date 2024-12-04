**Example 1: 设置主题属性**



Input: 

```
tccli ckafka ModifyTopicAttributes --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Note note \
    --TopicName topic-test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "fcfb7c89-3973-44f1-9a3e-a2811c67434e"
    }
}
```

