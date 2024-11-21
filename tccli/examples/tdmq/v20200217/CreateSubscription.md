**Example 1: 创建订阅关系**



Input: 

```
tccli tdmq CreateSubscription --cli-unfold-argument  \
    --EnvironmentId devNs \
    --TopicName devTopic \
    --SubscriptionName devSub \
    --Remark devTest \
    --IsIdempotent True \
    --ClusterId pulsar-5r59xd4vnx \
    --AutoCreatePolicyTopic True \
    --PostFixPattern LEGACY
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "15288803-dadb-4499-9b5b-ff2f631ca68e"
    }
}
```

