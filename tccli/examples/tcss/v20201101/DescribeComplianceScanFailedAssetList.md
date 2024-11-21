**Example 1: 查询上次检测失败的资产的列表**



Input: 

```
tccli tcss DescribeComplianceScanFailedAssetList --cli-unfold-argument  \
    --AssetTypeSet ASSET_CONTAINER \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a",
        "TotalCount": 1,
        "ScanFailedAssetList": [
            {
                "CustomerAssetId": 111456789,
                "AssetType": "ASSET_CONTAINDER",
                "AssetName": "happy-jenkins",
                "CheckStatus": "CHECK_FINISHED",
                "CheckTime": "2021-04-02 16:42:00",
                "FailureReason": "发生一些预料之外的情况",
                "Suggestion": "尝试重试"
            }
        ]
    }
}
```

