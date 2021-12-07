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

