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
                "AssetCount": 37,
                "AssetType": "云服务器",
                "CheckType": "network_security",
                "CreateTime": "2025-04-29T08:51:33Z",
                "EventType": "云服务器安全组IP来源设置过大",
                "Provider": "腾讯云",
                "RiskCount": 67,
                "RiskDesc": "发现*个云服务器安全组IP来源设置过大",
                "RiskRuleId": "tc_003",
                "RiskStatus": 0,
                "RiskTitle": "云服务器安全组IP来源设置过大",
                "Severity": "medium",
                "UpdateTime": "2025-05-07T01:51:30Z"
            }
        ],
        "RequestId": "3ac59d59-0a8e-4c6a-8249-936f0f02cf99",
        "TotalCount": 32
    }
}
```

