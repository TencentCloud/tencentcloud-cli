**Example 1: 检查视角下云资源配置风险列表**



Input: 

```
tccli csip DescribeCheckViewRisks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CheckViewRiskList": [
            {
                "AssetCount": 2,
                "AssetType": "u5b58u50a8u6876",
                "CheckType": "auth_control",
                "Classify": "emergency",
                "CreateTime": "2025-11-04 12:09:42",
                "EventType": "COSu5b58u50a8u6876u8bbfu95eeu6743u9650u914du7f6eu4e0du5f53",
                "Provider": "u817eu8bafu4e91",
                "RiskCount": 2,
                "RiskDesc": "u53d1u73b0*u4e2aCOSu5b58u50a8u6876u8bbfu95eeu6743u9650u914du7f6eu4e0du5f53",
                "RiskRuleId": "tc_072",
                "RiskStatus": 0,
                "RiskTitle": "COSu5b58u50a8u6876u8bbfu95eeu6743u9650u914du7f6eu4e0du5f53",
                "Severity": "high",
                "UpdateTime": "2025-11-12 16:15:30"
            }
        ],
        "TotalCount": 32,
        "RequestId": "cdf1d564-f937-4f9a-a290-8ff9e989f222"
    }
}
```

