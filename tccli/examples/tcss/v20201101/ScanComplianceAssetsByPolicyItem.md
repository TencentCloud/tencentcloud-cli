**Example 1: 用指定的检测项重新检测选定的资产**



Input: 

```
tccli tcss ScanComplianceAssetsByPolicyItem --cli-unfold-argument  \
    --CustomerPolicyItemId 10001 \
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

