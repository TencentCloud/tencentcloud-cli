**Example 1: 查询上次任务的资产通过率汇总信息**



Input: 

```
tccli tcss DescribeComplianceTaskAssetSummary --cli-unfold-argument  \
    --AssetTypeSet ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "Status": "USER_NORMAL",
        "AssetSummaryList": [
            {
                "AssetType": "ASSET_CONTAINER",
                "IsCustomerFirstCheck": true,
                "CheckStatus": "CHECK_FINISHED",
                "LastCheckTime": "2021-04-02 16:42:00",
                "CheckCostTime": 300,
                "CheckProgress": 100,
                "PeriodRule": {
                    "ExecutionTime": "xx",
                    "Frequency": 1
                },
                "PassedPolicyItemCount": 100,
                "FailedPolicyItemCount": 10,
                "FailedCriticalPolicyItemCount": 1,
                "FailedHighRiskPolicyItemCount": 2,
                "FailedMediumRiskPolicyItemCount": 1,
                "FailedLowRiskPolicyItemCount": 1,
                "NoticePolicyItemCount": 1,
                "PassedAssetCount": 1000,
                "FailedAssetCount": 100,
                "AssetPassedRate": 91,
                "ScanFailedAssetCount": 1
            }
        ]
    }
}
```

