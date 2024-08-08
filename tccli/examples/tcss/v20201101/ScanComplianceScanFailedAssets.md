**Example 1: 重新检测上次检测失败的资产**



Input: 

```
tccli tcss ScanComplianceScanFailedAssets --cli-unfold-argument  \
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

**Example 2: 再次扫描失败资产**

再次扫描失败资产

Input: 

```
tccli tcss ScanComplianceScanFailedAssets --cli-unfold-argument  \
    --CustomerAssetIdSet 2202462 \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "03546211-26e8-47d0-92f4-ed8250df32c5",
        "TaskId": 2538
    }
}
```

