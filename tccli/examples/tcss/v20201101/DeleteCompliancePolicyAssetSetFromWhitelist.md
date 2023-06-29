**Example 1: 忽略检测项+资产列表**



Input: 

```
tccli tcss DeleteCompliancePolicyAssetSetFromWhitelist --cli-unfold-argument  \
    --PolicyAssetSetList.0.CustomerPolicyItemId 1 \
    --PolicyAssetSetList.0.CustomerAssetItemIdSet 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

