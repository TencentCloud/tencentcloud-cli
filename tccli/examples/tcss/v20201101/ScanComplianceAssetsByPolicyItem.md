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

**Example 2: 检测策略下资产**

检测策略下资产

Input: 

```
tccli tcss ScanComplianceAssetsByPolicyItem --cli-unfold-argument  \
    --CustomerPolicyItemId 2798 \
    --CustomerAssetIdSet 2202462 \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "1f25995a-d6f2-4b3d-aea5-719288998970",
        "TaskId": 2540
    }
}
```

