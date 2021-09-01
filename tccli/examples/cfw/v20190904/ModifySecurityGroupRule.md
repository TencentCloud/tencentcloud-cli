**Example 1: 编辑单条安全组规则**

编辑单条安全组规则

Input: 

```
tccli cfw ModifySecurityGroupRule --cli-unfold-argument  \
    --SgRuleOriginSequence 1 \
    --Direction 1 \
    --Enable 1 \
    --Data.0.TargetType 1 \
    --Data.0.BothWay 1 \
    --Data.0.SourceId xx \
    --Data.0.Detail xx \
    --Data.0.Strategy 1 \
    --Data.0.Id 1 \
    --Data.0.Status 1 \
    --Data.0.Direction 1 \
    --Data.0.VpcId xx \
    --Data.0.IsNew 1 \
    --Data.0.TargetId xx \
    --Data.0.SubnetId xx \
    --Data.0.Cidr xx \
    --Data.0.ServiceTemplateId xx \
    --Data.0.OrderIndex 1 \
    --Data.0.InstanceName xx \
    --Data.0.Protocol xx \
    --Data.0.SourceType 1 \
    --Data.0.BothWayInfo xx \
    --Data.0.PrivateIp xx \
    --Data.0.PublicIp xx \
    --Data.0.Port xx
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "Status": 0,
        "NewRuleId": 35641
    }
}
```

