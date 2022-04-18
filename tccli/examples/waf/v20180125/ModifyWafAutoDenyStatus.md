**Example 1: 配置WAF自动情报封禁模块详情**



Input: 

```
tccli waf ModifyWafAutoDenyStatus --cli-unfold-argument  \
    --WafAutoDenyDetails.TimeThreshold 0 \
    --WafAutoDenyDetails.AttackThreshold 0 \
    --WafAutoDenyDetails.AttackTags 123 \
    --WafAutoDenyDetails.DefenseStatus 0
```

Output: 
```
{
    "Response": {
        "WafAutoDenyDetails": {
            "TimeThreshold": 0,
            "AttackThreshold": 0,
            "AttackTags": [
                "123"
            ],
            "DefenseStatus": 0
        },
        "RequestId": "xx"
    }
}
```

