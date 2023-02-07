**Example 1: 发送消息**

发送消息

Input: 

```
tccli ckafka SendMessageByTopic --cli-unfold-argument  \
    --InstanceId xx \
    --Message xx \
    --Partition 0 \
    --TopicName xx \
    --Key xx
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

