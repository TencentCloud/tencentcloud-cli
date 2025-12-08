**Example 1: 发送消费**

发送消息

Input: 

```
tccli trocket SendMessage --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Topic topic \
    --MsgBody testBody \
    --MsgKey testKey \
    --MsgTag testTag
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "MsgId": "1EAE3915000721B8D17C2C5BB31638D1",
        "RequestId": "256f8223-d0e2-4400-9481-763989799560"
    }
}
```

