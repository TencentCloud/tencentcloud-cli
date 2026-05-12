**Example 1: 查询Dspm资产id列表**



Input: 

```
tccli csip DescribeDspmAssetIds --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AssetSet": [
            {
                "Id": 1,
                "AssetId": "cdb-c2thbt00",
                "AssetType": "cdb",
                "Name": "测试cdb"
            }
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

