**Example 1: 操作资产关联的标签**



Input: 

```
tccli csip ModifyAssetTags --cli-unfold-argument  \
    --MemberId mem-6wfo123 \
    --AssetRIDs 619dfa1365a76aba4dbbdfa516de10f0 \
    --TagIDs 12
```

Output: 
```
{
    "Response": {
        "Code": "0",
        "Message": "Asset tags updated successfully",
        "RequestId": "35df9d31-c6e0-41b3-ba10-56d2ac706262"
    }
}
```

