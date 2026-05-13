**Example 1: 恢复Dspm资产账号**



Input: 

```
tccli csip RevertDspmAssetAccount --cli-unfold-argument  \
    --AssetId cdb-c2thbt00 \
    --Account dspm_blob \
    --Host % \
    --PrivilegeFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

