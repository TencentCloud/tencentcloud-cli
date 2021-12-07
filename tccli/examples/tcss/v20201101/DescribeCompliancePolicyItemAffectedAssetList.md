**Example 1: 查询检测项影响的资产列表**



Input: 

```
tccli tcss DescribeCompliancePolicyItemAffectedAssetList --cli-unfold-argument  \
    --CustomerPolicyItemId 12345 \
    --Offset 1000 \
    --Limit 10 \
    --Filters.0.Name NodeName \
    --Filters.0.Values node-1 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TotalCount": 10,
        "AffectedAssetList": [
            {
                "CustomerAssetId": 10001,
                "AssetName": "happy-jenkins",
                "AssetType": "ASSET_CONTAINDER",
                "CheckStatus": "CHECK_FINISHED",
                "NodeName": "worker-node-1",
                "LastCheckTime": "2021-04-02 16:42:00",
                "CheckResult": "RESULT_PASSED"
            }
        ]
    }
}
```

