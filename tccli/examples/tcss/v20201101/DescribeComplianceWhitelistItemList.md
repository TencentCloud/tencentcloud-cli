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
        "RequestId": "xxxxx",
        "TotalCount": 1,
        "WhitelistItemSet": [
            {
                "WhitelistItemId": 123,
                "CustomerPolicyItemId": 456,
                "Name": "xxxx",
                "StandardId": 123,
                "StandardName": "CIS Docker",
                "AffectedAssetCount": 100,
                "LastUpdateTime": "2021-04-02 16:00:00",
                "InsertTime": "2021-04-02 16:00:00"
            }
        ]
    }
}
```

