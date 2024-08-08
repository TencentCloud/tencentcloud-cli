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

**Example 2: 忽略资产未通过检测项**

忽略资产未通过检测项

Input: 

```
tccli tcss AddComplianceAssetPolicySetToWhitelist --cli-unfold-argument  \
    --AssetPolicySetList.0.CustomerAssetItemId 2202462 \
    --AssetPolicySetList.0.CustomerPolicyItemIdSet 2809 \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "5728fa7b-e88a-4cb0-aabb-a403c470ca36"
    }
}
```

