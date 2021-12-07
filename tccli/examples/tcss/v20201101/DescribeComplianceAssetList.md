**Example 1: 查询某类资产的列表**



Input: 

```
tccli tcss DescribeComplianceAssetList --cli-unfold-argument  \
    --AssetTypeSet ASSET_CONTAINDER \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TotalCount": 1,
        "AssetInfoList": [
            {
                "CustomerAssetId": 123456789,
                "AssetType": "ASSET_CONTAINDER",
                "AssetName": "happy-jekins",
                "NodeName": "worker-node-1",
                "CheckStatus": "CHECK_FINISHED",
                "LastCheckTime": "2021-04-02 16:42:00",
                "PassedPolicyItemCount": 100,
                "FailedPolicyItemCount": 10,
                "CheckResult": "RESULT_PASSED"
            }
        ]
    }
}
```

