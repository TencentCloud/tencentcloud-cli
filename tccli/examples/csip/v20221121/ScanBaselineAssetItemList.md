**Example 1: 扫描资产风险**

扫描资产风险

Input: 

```
tccli csip ScanBaselineAssetItemList --cli-unfold-argument  \
    --PolicyType SELF \
    --PolicyID 2 \
    --CategoryID 2 \
    --ParentCategoryID 1 \
    --ItemIDList 124 \
    --AssetID instance-1 \
    --MemberId mem-***********795752f66e429 \
    --AssetType HOST
```

Output: 
```
{
    "Response": {
        "RequestId": "7a2bc5a9-0ad7-4c4b-8d83-20eea24da7e6"
    }
}
```

