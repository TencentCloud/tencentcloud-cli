**Example 1: 资产统一搜索**



Input: 

```
tccli databuddy SearchAsset --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --MaxResults 1 \
    --Keyword order
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Aliases": [],
                    "AssetGuid": "hooke.zhangyue_test.order_detail_0@*********_ap-guangzhou_TABLE",
                    "AssetId": "hooke.zhangyue_test.order_detail_0",
                    "AssetName": "order_detail_0",
                    "AssetType": "TABLE",
                    "CatalogSource": "CONNECTION",
                    "Comment": "",
                    "FieldInfo": [
                        {
                            "Comment": "",
                            "Content": "",
                            "Lang": "",
                            "Name": "order_id",
                            "SampleValues": [],
                            "Type": "long"
                        }
                    ],
                    "FieldTags": [],
                    "FullName": "hooke.zhangyue_test.order_detail_0",
                    "HighlightingInfo": {
                        "AliasFragments": [],
                        "AssetName": "<em>order</em>_detail_0",
                        "CodeFragments": [],
                        "Comment": "",
                        "FullName": "",
                        "TagFragments": [],
                        "TextFragments": [
                            {
                                "Comment": "",
                                "Content": "",
                                "Lang": "",
                                "Name": "<em>order</em>_id",
                                "Type": "long"
                            }
                        ]
                    },
                    "ModifiedTime": "1790129153387",
                    "Owner": {
                        "Type": 0,
                        "UserId": "",
                        "UserName": ""
                    },
                    "Popularity": "1",
                    "PopularityQuantity": "0",
                    "Properties": [],
                    "Tags": [],
                    "UserActivityInfo": {
                        "IsFavorite": false,
                        "LastViewTime": ""
                    },
                    "WorkspaceId": "",
                    "WorkspacePath": ""
                }
            ],
            "NextPageToken": "eyJzZWFyY2hBZnRlclZhbHVlcyI6WzE4LjE5NTgxNiwiaG9va2Uuemhhbmd5dWVfdGVzdC5vcmRlcl9kZXRhaWxfMEAyNjAwNzM0OTNfYXAtZ3Vhbmd6aG91X1RBQkxFIl19"
        },
        "RequestId": "14c44330-20d2-441e-95f7-12c3b56d56e0"
    }
}
```

