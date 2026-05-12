**Example 1: 查询Dspm资产支持的权限**



Input: 

```
tccli csip DescribeDspmAssetSupportedPrivileges --cli-unfold-argument  \
    --AssetId cdb-c2thbt00
```

Output: 
```
{
    "Response": {
        "GlobalSupportedPrivileges": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE"
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

