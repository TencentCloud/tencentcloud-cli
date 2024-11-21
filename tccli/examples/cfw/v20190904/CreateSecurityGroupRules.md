**Example 1: 创建企业安全组规则**

创建企业安全组规则

Input: 

```
tccli cfw CreateSecurityGroupRules --cli-unfold-argument  \
    --Data.0.BothWay 0 \
    --Data.0.BothWayInfo.0.OrderIndex 1 \
    --Data.0.BothWayInfo.0.SourceId 1.1.1.1 \
    --Data.0.BothWayInfo.0.SourceType 7 \
    --Data.0.BothWayInfo.0.TargetId 1.1.1.1 \
    --Data.0.BothWayInfo.0.TargetType 2 \
    --Data.0.BothWayInfo.0.Protocol ANY \
    --Data.0.BothWayInfo.0.Port -1/-1 \
    --Data.0.BothWayInfo.0.Strategy 2 \
    --Data.0.BothWayInfo.0.Detail andy的规则 \
    --Data.0.BothWayInfo.0.Status 1 \
    --Data.0.BothWayInfo.0.IsNew 1 \
    --Data.0.BothWayInfo.0.BothWay 0 \
    --Data.0.BothWayInfo.0.VpcId vpc-iedpwx01d \
    --Data.0.BothWayInfo.0.SubnetId subnet-ed2witec \
    --Data.0.BothWayInfo.0.InstanceName andy的cvm \
    --Data.0.BothWayInfo.0.PublicIp 1.1.1.1 \
    --Data.0.BothWayInfo.0.PrivateIp 1.1.1.1 \
    --Data.0.BothWayInfo.0.Cidr 10.72.1.0/24 \
    --Data.0.BothWayInfo.0.ServiceTemplateId pp-peodxd0e \
    --Data.0.BothWayInfo.0.Direction 1 \
    --Data.0.BothWayInfo.0.Region ap-guangzhou \
    --Data.0.BothWayInfo.0.ProtocolPortType 1 \
    --Data.0.Detail ignore 188.188.188.188 \
    --Data.0.Direction 1 \
    --Data.0.OrderIndex 1 \
    --Data.0.Port -1/-1 \
    --Data.0.Protocol ANY \
    --Data.0.ProtocolPortType 0 \
    --Data.0.ServiceTemplateId pp-peodxd0e \
    --Data.0.SourceId 188.188.188.188 \
    --Data.0.SourceType 0 \
    --Data.0.Strategy 2 \
    --Data.0.TargetId 0.0.0.0/0 \
    --Data.0.TargetType 9 \
    --Direction 1 \
    --Enable 1 \
    --Type 0
```

Output: 
```
{
    "Response": {
        "RequestId": "upykdsac-5aac-edd2-4f92-eebfa1a51efb",
        "Status": 0
    }
}
```

