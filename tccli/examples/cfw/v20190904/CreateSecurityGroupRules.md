**Example 1: 创建企业安全组规则**

创建企业安全组规则

Input: 

```
tccli cfw CreateSecurityGroupRules --cli-unfold-argument  \
    --Data.0.OrderIndex 1 \
    --Data.0.SourceId ipm-dyodhpby \
    --Data.0.TargetId subnet-fmo10koi \
    --Data.0.Protocol ANY \
    --Data.0.Port -1/-1 \
    --Data.0.ServiceTemplateId ppm-9olqf3lc \
    --Data.0.Strategy 2 \
    --Data.0.Detail test 555 \
    --Data.0.VpcId vpc-8xuf8kf5 \
    --Data.0.SubnetId subnet-fmo10koi \
    --Data.0.BothWay 0 \
    --Data.0.BothWayInfo  \
    --Data.0.SourceType 7 \
    --Data.0.TargetType 2 \
    --Data.0.Direction 1 \
    --Data.1.OrderIndex 2 \
    --Data.1.SourceId ipmg-43isdfuc \
    --Data.1.TargetId subnet-5cwgmy1i \
    --Data.1.Protocol ANY \
    --Data.1.Port -1/-1 \
    --Data.1.ServiceTemplateId ppmg-jz17vpis \
    --Data.1.Strategy 2 \
    --Data.1.Detail test 555 \
    --Data.1.VpcId vpc-aa6b04jr \
    --Data.1.SubnetId subnet-5cwgmy1i \
    --Data.1.BothWay 0 \
    --Data.1.BothWayInfo  \
    --Data.1.SourceType 7 \
    --Data.1.TargetType 2 \
    --Data.1.Direction 1 \
    --Type 0 \
    --Enable 1 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "Status": 0
    }
}
```

