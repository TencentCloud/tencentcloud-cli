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

