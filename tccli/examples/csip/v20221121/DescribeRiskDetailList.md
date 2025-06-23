**Example 1: 风险详情列表**



Input: 

```
tccli csip DescribeRiskDetailList --cli-unfold-argument  \
    --RiskRuleId tc_001
```

Output: 
```
{
    "Response": {
        "AssetRiskDetailList": [
            {
                "CheckStatus": "",
                "CloudAccountId": "12352343",
                "CloudAccountName": "测试",
                "CreateTime": "2025-04-29T07:36:22Z",
                "InstanceId": "12352343",
                "InstanceName": "test",
                "Provider": "tencent",
                "ProviderName": "腾讯云",
                "RiskContent": "{\"header\": [{\"name\": \"user_name\", \"value\": \"用户名称\"}, {\"name\": \"console_login\", \"value\": \"是否可以登录控制台\"}, {\"name\": \"user_uin\", \"value\": \"用户账号\"}, {\"name\": \"risk_type\", \"value\": \"风险类型\"}], \"result\": {\"user_name\": \"test\", \"console_login\": \"是\", \"risk_type\": \"操作保护未开启\", \"user_uin\": \"123423131\"}}",
                "RiskId": 1,
                "RiskRuleId": "tc_001",
                "RiskStatus": 0,
                "UpdateTime": "2025-05-07T01:51:26Z"
            }
        ],
        "RequestId": "f3d556f8-9168-4a7c-b839-b0d8d07a706d",
        "TotalCount": 1
    }
}
```

