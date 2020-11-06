**Example 1: 设置主题属性**



Input: 

```
tccli ckafka ModifyTopicAttributes --cli-unfold-argument  \
    --InstanceId xxx \
    --TopicName xxx \
    --Note xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply success]"
        },
        "RequestId": "83d1142c-2754-46fb-99ca-46d9d87f5e3e"
    }
}
```

