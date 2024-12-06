**Example 1: 修改订阅属性**



Input: 

```
tccli tdmq ModifyCmqSubscriptionAttribute --cli-unfold-argument  \
    --TopicName check-topic \
    --SubscriptionName check-sub \
    --NotifyStrategy BACKOFF_RETRY \
    --FilterTags ins
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

