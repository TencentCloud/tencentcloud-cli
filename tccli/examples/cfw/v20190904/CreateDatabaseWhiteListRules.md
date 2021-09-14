**Example 1: 创建暴露数据库白名单规则**



Input: 

```
tccli cfw CreateDatabaseWhiteListRules --cli-unfold-argument  \
    --DatabaseWhiteListRuleData.0.SourceIp 0.0.0.0/0 \
    --DatabaseWhiteListRuleData.0.SourceType 1 \
    --DatabaseWhiteListRuleData.0.TargetIp 119.29.186.197 \
    --DatabaseWhiteListRuleData.0.TargetType 1 \
    --DatabaseWhiteListRuleData.0.Detail test \
    --DatabaseWhiteListRuleData.0.Enable 1 \
    --DatabaseWhiteListRuleData.0.IsRegionRule 0 \
    --DatabaseWhiteListRuleData.0.IsCloudRule 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

