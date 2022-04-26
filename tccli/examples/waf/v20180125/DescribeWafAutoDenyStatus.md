**Example 1: 描述WAF自动封禁模块详情**



Input: 

```
tccli waf DescribeWafAutoDenyStatus --cli-unfold-argument ```

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

