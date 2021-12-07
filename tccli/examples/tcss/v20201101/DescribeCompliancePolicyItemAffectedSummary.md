**Example 1: 查询某检测项影响的信息**



Input: 

```
tccli tcss DescribeCompliancePolicyItemAffectedSummary --cli-unfold-argument  \
    --CustomerPolicyItemId 12345
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "PolicyItemSummary": {
            "CustomerPolicyItemId": 10001,
            "BasePolicyItemId": 1,
            "Name": "审计Docker文件和目录",
            "Category": "xxx",
            "BenchmarkStandardName": "CIS_Docker",
            "BenchmarkStandardId": 123,
            "RiskLevel": "xx",
            "AssetType": "xxx",
            "CheckStatus": "",
            "CheckResult": "xx",
            "LastCheckTime": "2020-09-22 00:00:00",
            "PassedAssetCount": 100,
            "FailedAssetCount": 20,
            "WhitelistId": 12345,
            "FixSuggestion": "xxxx"
        }
    }
}
```

