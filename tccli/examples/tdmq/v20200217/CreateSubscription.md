**Example 1: 创建订阅关系**



Input: 

```
tccli tdmq CreateSubscription --cli-unfold-argument  \
    --EnvironmentId default \
    --Remark 创建订阅关系 \
    --IsIdempotent true \
    --TopicName cloud_test \
    --SubscriptionName cloud_sub \
    --AutoCreatePolicyTopic true
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

