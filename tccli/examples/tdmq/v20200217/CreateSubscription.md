**Example 1: 创建订阅关系**



Input: 

```
tccli tdmq CreateSubscription --cli-unfold-argument  \
    --EnvironmentId abc \
    --TopicName abc \
    --SubscriptionName abc \
    --Remark abc \
    --IsIdempotent True \
    --ClusterId abc \
    --AutoCreatePolicyTopic True \
    --PostFixPattern abc
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

