**Example 1: 忽略检测项+资产列表**



Input: 

```
tccli tcss DeleteComplianceAssetPolicySetFromWhitelist --cli-unfold-argument  \
    --AssetItemId 10001 \
    --CustomerPolicyItemIdSet 10001 10002
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 取消资产忽略项**

取消资产忽略项

Input: 

```
tccli tcss DeleteComplianceAssetPolicySetFromWhitelist --cli-unfold-argument  \
    --AssetItemId 2202462 \
    --CustomerPolicyItemIdSet 2809 \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "925e6419-1fb8-4169-a96c-020e3ae9171e"
    }
}
```

