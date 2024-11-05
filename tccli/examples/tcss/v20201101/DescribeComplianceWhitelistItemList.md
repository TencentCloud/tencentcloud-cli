**Example 1: 查询白名单列表**



Input: 

```
tccli tcss DescribeComplianceWhitelistItemList --cli-unfold-argument  \
    --AssetTypeSet ASSET_IMAGE \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a",
        "TotalCount": 1,
        "WhitelistItemSet": [
            {
                "WhitelistItemId": 1001,
                "CustomerPolicyItemId": 456,
                "Name": "test-name",
                "StandardId": 11222,
                "StandardName": "CIS Docker",
                "AffectedAssetCount": 100,
                "LastUpdateTime": "2021-04-02 16:00:00",
                "InsertTime": "2021-04-02 16:00:00"
            }
        ]
    }
}
```

