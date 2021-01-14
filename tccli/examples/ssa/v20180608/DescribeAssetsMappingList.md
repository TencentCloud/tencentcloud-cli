**Example 1: 资产测绘-测绘列表**



Input: 

```
tccli ssa DescribeAssetsMappingList --cli-unfold-argument  \
    --Params test
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetIp": "1.1.1.1",
                "AssetName": "asset-name",
                "Instid": "inst-id",
                "AssetType": "asset-type-value",
                "AssetRegionEn": "test",
                "AssetRegionCn": "测试",
                "AssetNetwork": "xxx",
                "AssetStatusEn": "xxx",
                "AssetStatusCn": "xxx",
                "IsWhite": "True",
                "Status": "running",
                "Time": "2020-12-12 12:12:00",
                "Tag": [
                    {
                        "Fid": "fid",
                        "Fname": "fname"
                    }
                ],
                "Group": [
                    "A",
                    "B"
                ],
                "Port": "8080",
                "Component": "xxx",
                "AssetInstanceType": "xxx",
                "IsIntranet": 1
            }
        ],
        "TotalCount": 1,
        "CountByType": "test",
        "RequestId": "70442e41-d391-4226-aef0-659360c8e9df"
    }
}
```

