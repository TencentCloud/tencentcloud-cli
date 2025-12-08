**Example 1: 修改名字空间**



Input: 

```
tccli tdmq ModifyEnvironmentAttributes --cli-unfold-argument  \
    --EnvironmentId shanxuTest \
    --MsgTTL 60 \
    --ClusterId pulsar-zaxdmeegvgee \
    --SubscriptionExpirationTime 1440 \
    --SubscriptionExpirationTimeEnable True
```

Output: 
```
{
    "Response": {
        "EnvironmentId": "shanxuTest",
        "MsgTTL": 60,
        "NamespaceId": "ns-jakba8kdbrno",
        "Remark": "createSubscriptionExpirationtest",
        "SubscriptionExpirationTime": 1440,
        "SubscriptionExpirationTimeEnable": true,
        "RequestId": "4664945f-0d01-4da7-8dd8-5274bb4d4c8a"
    }
}
```

