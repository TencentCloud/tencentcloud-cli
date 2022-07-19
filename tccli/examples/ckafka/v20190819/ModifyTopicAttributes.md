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

