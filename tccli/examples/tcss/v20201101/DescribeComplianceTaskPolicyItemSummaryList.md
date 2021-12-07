**Example 1: 查询上次任务的检测项的汇总信息列表**



Input: 

```
tccli tcss DescribeComplianceTaskPolicyItemSummaryList --cli-unfold-argument  \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TaskId": 123456,
        "TotalCount": 123,
        "PolicyItemSummaryList": [
            {
                "CustomerPolicyItemId": 10001,
                "BasePolicyItemId": 1,
                "Name": "审计Docker文件和目录",
                "Category": "xxx",
                "BenchmarkStandardName": "CIS_Docker",
                "BenchmarkStandardId": 123,
                "RiskLevel": "xx",
                "AssetType": "xxx",
                "LastCheckTime": "2020-09-22 00:00:00",
                "CheckStatus": "CHECK_FINISHED",
                "CheckResult": "xx",
                "PassedAssetCount": 100,
                "FailedAssetCount": 20,
                "WhitelistId": 12345,
                "FixSuggestion": "xxxx"
            }
        ]
    }
}
```

