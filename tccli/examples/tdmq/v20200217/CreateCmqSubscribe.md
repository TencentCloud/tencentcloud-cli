**Example 1: 创建订阅接口**



Input: 

```
tccli tdmq CreateCmqSubscribe --cli-unfold-argument  \
    --TopicName ConnTopic \
    --SubscriptionName ConnSubQueue \
    --Protocol queue \
    --Endpoint queue_sub
```

Output: 
```
{
    "Response": {
        "SubscriptionId": "subsc-39gyuuhd",
        "RequestId": "1620b635-6071-47c7-ac1e-975afe5104a7"
    }
}
```

