**Example 1: 查询某资产下的检测项列表**



Input: 

```
tccli tcss DescribeComplianceAssetPolicyItemList --cli-unfold-argument  \
    --CustomerAssetId 123456 \
    --Offset 10 \
    --Limit 10 \
    --Filters.0.Name RiskLevel \
    --Filters.0.Values RISK_CRITICAL RISK_HIGH \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TotalCount": 123,
        "AssetPolicyItemList": [
            {
                "CustomerPolicyItemId": 10001,
                "BasePolicyItemId": 1,
                "Name": "审计Docker文件和目录",
                "Category": "xxx",
                "BenchmarkStandardId": 123,
                "BenchmarkStandardName": "CIS Docker",
                "RiskLevel": "RISK_HIGH",
                "CheckStatus": "CHECK_FINISHED",
                "CheckResult": "RESULT_FAILED",
                "WhitelistId": 12345,
                "FixSuggestion": "xxxx",
                "LastCheckTime": "2021-04-02 16:00:00"
            }
        ]
    }
}
```

