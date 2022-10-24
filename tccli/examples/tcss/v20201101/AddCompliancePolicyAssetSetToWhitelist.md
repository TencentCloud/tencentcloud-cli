**Example 1: 忽略检测项+资产列表**



Input: 

```
tccli tcss AddCompliancePolicyAssetSetToWhitelist --cli-unfold-argument  \
    --CustomerPolicyItemId 10001 \
    --CustomerAssetItemIdSet 10001 10002
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

