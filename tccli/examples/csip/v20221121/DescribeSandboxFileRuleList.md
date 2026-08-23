**Example 1: 调用示例**



Input: 

```
tccli csip DescribeSandboxFileRuleList --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "RuleList": [
            {
                "RuleContent": {
                    "Action": "RO",
                    "BelongAssetType": "HOST",
                    "EffectScope": {
                        "EffectAssets": [],
                        "EffectType": "EXCLUDE"
                    },
                    "PathWhitelist": [
                        "/home/dev/.local/bin"
                    ],
                    "RuleName": "allow dot local bin",
                    "Status": "ON"
                },
                "RuleID": 2,
                "RuleType": "CUSTOM",
                "UpdateTime": "2026-04-26T06:22:35Z"
            }
        ],
        "TotalCount": 2,
        "RequestId": "a51b3fc4-cb94-4ada-b23e-1f8401f79bd2"
    }
}
```

