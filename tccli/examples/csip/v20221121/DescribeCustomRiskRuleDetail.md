**Example 1: 自定义风险规则配置详情列表**



Input: 

```
tccli csip DescribeCustomRiskRuleDetail --cli-unfold-argument  \
    --RuleID tc_002
```

Output: 
```
{
    "Response": {
        "CustomRiskRuleDetailList": [
            {
                "AppID": 13004999112,
                "Status": "disable"
            }
        ],
        "RequestId": "72c776a0-f948-4c5d-ac61-09aee26d6856"
    }
}
```

