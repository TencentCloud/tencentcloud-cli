**Example 1: 发布广播消息**



Input: 

```
tccli iotcloud PublishBroadcastMessage --cli-unfold-argument  \
    --ProductId ASBHKN121 \
    --Payload 123456 \
    --Qos 1
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e",
        "TaskId": 1000523
    }
}
```

