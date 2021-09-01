**Example 1: 确认消息**



Input: 

```
tccli tdmq AcknowledgeMessage --cli-unfold-argument  \
    --AckTopic tenant/namespace/topic \
    --MessageId "71:12:0" \
    --SubName “test-sub”
```

Output: 
```
{
    "Response": {
        "RequestId": "36713f94-d07d-4b96-babf-42d139276f23",
        "ErrorMsg": "xxx"
    }
}
```

