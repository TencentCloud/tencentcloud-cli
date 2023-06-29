**Example 1: 忽略检测项+资产列表**



Input: 

```
tccli tcss AddComplianceAssetPolicySetToWhitelist --cli-unfold-argument  \
    --AssetPolicySetList.0.CustomerPolicyItemIdSet 1 \
    --AssetPolicySetList.0.CustomerAssetItemId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

