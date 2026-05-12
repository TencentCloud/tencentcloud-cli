**Example 1: 查询Dspm资产账号预设特权信息**



Input: 

```
tccli csip DescribeDspmAssetAccountPresetPrivileges --cli-unfold-argument  \
    --AssetId cdb-dgtiaz1q \
    --Account root \
    --Host %
```

Output: 
```
{
    "Response": {
        "Privilege": {},
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

