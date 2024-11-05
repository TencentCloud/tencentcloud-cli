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
        "Status": "USER_NORMAL",
        "AssetSummaryList": [
            {
                "AssetType": "ASSET_CONTAINER",
                "IsCustomerFirstCheck": true,
                "CheckStatus": "CHECK_FINISHED",
                "CheckProgress": 0,
                "PassedPolicyItemCount": 1,
                "FailedPolicyItemCount": 1,
                "FailedCriticalPolicyItemCount": 1,
                "FailedHighRiskPolicyItemCount": 1,
                "FailedMediumRiskPolicyItemCount": 1,
                "FailedLowRiskPolicyItemCount": 1,
                "NoticePolicyItemCount": 1,
                "PassedAssetCount": 1,
                "FailedAssetCount": 1,
                "AssetPassedRate": 0,
                "ScanFailedAssetCount": 1,
                "CheckCostTime": 0,
                "LastCheckTime": "2020-09-22 00:00:00",
                "PeriodRule": {
                    "Frequency": 1,
                    "ExecutionTime": "21:00",
                    "Enable": true
                },
                "OpenPolicyItemCount": 1,
                "IgnoredPolicyItemCount": 1,
                "TotalPolicyItemCount": 1,
                "DetectHostCount": 1,
                "LeftTime": 1
            }
        ],
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a"
    }
}
```

