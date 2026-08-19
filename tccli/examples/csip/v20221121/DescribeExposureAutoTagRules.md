**Example 1: 云边界分析自动打标规则**



Input: 

```
tccli csip DescribeExposureAutoTagRules --cli-unfold-argument  \
    --MemberId mem-000000 \
    --Limit 1 \
    --Offset 0 \
    --Order Desc \
    --By UpdateTime
```

Output: 
```
{
    "Response": {
        "RuleList": [
            {
                "AssetTypes": [],
                "CreateTime": "2026-07-08 17:17:33",
                "Description": "合理业务",
                "Enable": true,
                "OpenStatuses": [
                    "open"
                ],
                "Ports": [
                    "80"
                ],
                "Priority": 0,
                "RuleID": 1,
                "RuleName": "测试打标规则1",
                "Tag": "legit_business",
                "UpdateTime": "2026-07-09 09:53:17"
            }
        ],
        "TotalCount": 2,
        "RequestId": "0d3ffaf4-3251-4808-9717-80bd2c6262ac"
    }
}
```

