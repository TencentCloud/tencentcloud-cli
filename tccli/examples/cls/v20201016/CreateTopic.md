**Example 1: 创建日志主题**



Input: 

```
tccli cls CreateTopic --cli-unfold-argument  \
    --LogsetId 6b2c40ae-2bd0-445e-adf2-3129a59fb6d5 \
    --TopicName cloud_topic_test \
    --PartitionCount 1 \
    --AutoSplit True \
    --MaxSplitPartitions 10 \
    --StorageType hot \
    --Period 30 \
    --Describes 场景日志主题 \
    --BizType 0 \
    --IsSourceFrom False \
    --BillingMode 0
```

Output: 
```
{
    "Response": {
        "TopicId": "8aa25df8-6065-45de-8b3e-b65f8797e2a1",
        "RequestId": "cca37d5e-f542-44f4-a1bf-5fa09fb66439"
    }
}
```

**Example 2: 创建日志主题并打标签**



Input: 

```
tccli cls CreateTopic --cli-unfold-argument  \
    --LogsetId 7fb0245e-2006-4e0f-9153-c5f6b7110b4c \
    --TopicName business_log_test1 \
    --PartitionCount 1 \
    --Tags.0.Key business_log_key \
    --Tags.0.Value business_log_value \
    --AutoSplit True \
    --MaxSplitPartitions 3 \
    --StorageType hot \
    --Period 1 \
    --Describes 业务日志 \
    --BizType 0 \
    --IsWebTracking False \
    --Extends.AnonymousAccess.Operations realtimeProducer \
    --Extends.AnonymousAccess.Conditions.0.Attributes VpcID \
    --Extends.AnonymousAccess.Conditions.0.Rule 1 \
    --Extends.AnonymousAccess.Conditions.0.ConditionValue vpc-******** \
    --IsSourceFrom True \
    --BillingMode 0
```

Output: 
```
{
    "Response": {
        "TopicId": "6ce29951-838f-44de-a321-35e3e25798eb",
        "RequestId": "4207ca55-4498-4c6b-a329-d27c8c4fd144"
    }
}
```

