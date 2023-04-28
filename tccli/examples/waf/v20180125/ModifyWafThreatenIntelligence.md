**Example 1: 配置WAF威胁情报封禁模块详情**

配置管理WAF 威胁情报封禁模块

Input: 

```
tccli waf ModifyWafThreatenIntelligence --cli-unfold-argument  \
    --WafThreatenIntelligenceDetails.DefenseStatus 0 \
    --WafThreatenIntelligenceDetails.Tags abc
```

Output: 
```
{
    "Response": {
        "WafThreatenIntelligenceDetails": {
            "DefenseStatus": 0,
            "LastUpdateTime": "2020-09-22T00:00:00+00:00",
            "Tags": [
                "abc"
            ]
        },
        "RequestId": "cdf"
    }
}
```

