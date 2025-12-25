**Example 1: 资产视角下风险列表示例**



Input: 

```
tccli csip DescribeAssetRiskList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "StandardNameList": [],
        "AssetRiskList": [
            {
                "AppId": 1434332551,
                "CheckType": "network_security",
                "CloudAccountId": "12335421",
                "CloudAccountName": "天空之城",
                "CreateTime": "2025-04-29T08:51:39Z",
                "InstanceId": "ins-76tgxsoxi",
                "InstanceName": "AI验证",
                "Provider": "tencent",
                "ProviderName": "腾讯云",
                "RiskRuleId": "tc_191",
                "RiskStatus": 2,
                "RiskTitle": "安全组存在放通非业务端口全部网段的规则",
                "Severity": "medium",
                "Classify": "emergency",
                "UpdateTime": "2025-05-07T01:51:28Z"
            }
        ],
        "RequestId": "ab3a4f8f-30e4-462c-8be0-4b24bff70111",
        "TotalCount": 518
    }
}
```

