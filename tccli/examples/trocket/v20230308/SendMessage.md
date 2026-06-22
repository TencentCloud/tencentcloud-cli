**Example 1: 发送普通消息**



Input: 

```
tccli trocket SendMessage --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Topic test_topic \
    --MsgBody This is a normal message for Apache RocketMQ. \
    --MsgKey test_key \
    --MsgTag test_kag
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

**Example 2: 发送轻量消息**



Input: 

```
tccli trocket SendMessage --cli-unfold-argument  \
    --InstanceId rmq-16jm9787qv \
    --Topic test_topic_parent \
    --MsgBody This is a normal message for Apache RocketMQ. \
    --LiteTopic test_lite_topic
```

Output: 
```
{
    "Response": {
        "MsgId": "0B8D67BE00072D98A3357ED050E50000",
        "RequestId": "ac76f2f5-8ed0-4800-9cc2-c168e4a0e9a0"
    }
}
```

