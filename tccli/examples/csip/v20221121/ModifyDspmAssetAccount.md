**Example 1: 修改Dspm资产账号信息**



Input: 

```
tccli csip ModifyDspmAssetAccount --cli-unfold-argument  \
    --AssetId cdb-c2thbt00 \
    --Account root \
    --Host % \
    --AccountType 1 \
    --Remark 
```

Output: 
```
{
    "Response": {
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

