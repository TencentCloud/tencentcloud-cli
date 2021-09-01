**Example 1: 创建安全组API规则**



Input: 

```
tccli cfw CreateSecurityGroupApiRules --cli-unfold-argument  \
    --Data.0.SourceId 0.0.0.0/0 \
    --Data.0.TargetId 119.29.186.197 \
    --Data.0.Protocol ANY \
    --Data.0.Port -1/-1 \
    --Data.0.Strategy 1 \
    --Data.0.Detail test \
    --Data.0.RuleType 1 \
    --Type 0 \
    --Area  \
    --Direction 1
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

