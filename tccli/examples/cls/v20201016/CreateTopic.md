**Example 1: 创建日志主题**



Input: 

```
tccli cls CreateTopic --cli-unfold-argument  \
    --LogsetId 7fb0245e-2006-4e0f-9153-c5f6b7110b4c \
    --TopicName business_log_test \
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
        "TopicId": "aac1096a-cf02-4fe0-abcd-ddb89173b4e4",
        "RequestId": "487cd68f-d88f-4e35-888d-48612e8ff980"
    }
}
```

