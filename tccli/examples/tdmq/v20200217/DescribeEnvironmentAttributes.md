**Example 1: 查询命名空间详情**



Input: 

```
tccli tdmq DescribeEnvironmentAttributes --cli-unfold-argument  \
    --EnvironmentId felixsshi-ns \
    --ClusterId pulsar-35mrz4xb3az
```

Output: 
```
{
    "Response": {
        "EnvironmentId": "felixsshi-ns",
        "MsgTTL": 3600,
        "RateInByte": 52428800,
        "RateInSize": 0,
        "Remark": "",
        "Replicas": 2,
        "RetentionHours": 24,
        "RetentionSize": 10,
        "SubscriptionExpirationTime": 1440,
        "SubscriptionExpirationTimeEnable": true,
        "RequestId": "ded83ac0-49a9-4472-8a89-a05b193ead37"
    }
}
```

