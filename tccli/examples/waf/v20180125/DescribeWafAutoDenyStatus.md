**Example 1: 描述WAF自动封禁模块详情**



Input: 

```
tccli waf DescribeWafAutoDenyStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "WafAutoDenyDetails": {
            "AttackTags": [
                "idc"
            ],
            "AttackThreshold": 1,
            "DefenseStatus": 1,
            "TimeThreshold": 1,
            "DenyTimeThreshold": 1,
            "LastUpdateTime": "2020-09-22T00:00:00+00:00"
        },
        "RequestId": "053d6b22-87cd-4a12-ad89-8460e819ebf5"
    }
}
```

