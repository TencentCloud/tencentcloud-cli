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
        "TaskId": 1,
        "TotalCount": 1,
        "PolicyItemSummaryList": [
            {
                "CustomerPolicyItemId": 1,
                "BasePolicyItemId": 1,
                "Name": "abc",
                "Category": "abc",
                "BenchmarkStandardName": "abc",
                "RiskLevel": "abc",
                "AssetType": "abc",
                "LastCheckTime": "2020-09-22 00:00:00",
                "CheckStatus": "abc",
                "CheckResult": "abc",
                "PassedAssetCount": 1,
                "FailedAssetCount": 1,
                "WhitelistId": 1,
                "FixSuggestion": "abc",
                "BenchmarkStandardId": 1,
                "ApplicableVersion": "abc",
                "Description": "abc",
                "AuditProcedure": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

