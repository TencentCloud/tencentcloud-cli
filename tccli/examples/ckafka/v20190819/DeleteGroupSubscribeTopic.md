**Example 1: 删除消费分组订阅的主题**

删除不需要订阅的topic

Input: 

```
tccli ckafka DeleteGroupSubscribeTopic --cli-unfold-argument  \
    --InstanceId ckafka-inbijinh \
    --Group consuemr \
    --Topic topicName
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

