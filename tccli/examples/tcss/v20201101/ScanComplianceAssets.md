**Example 1: 重新扫描指定的资产**



Input: 

```
tccli tcss ScanComplianceAssets --cli-unfold-argument  \
    --CustomerAssetIdSet 123 456 789
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TaskId": 123
    }
}
```

**Example 2: 检测资产**

检测资产

Input: 

```
tccli tcss ScanComplianceAssets --cli-unfold-argument  \
    --CustomerAssetIdSet 2202462 \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "c8dda80e-f4bc-4a3a-a165-b81e4e4c9cb2",
        "TaskId": 2535
    }
}
```

