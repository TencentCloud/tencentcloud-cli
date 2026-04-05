**Example 1: 收藏V2列表**

收藏V2列表

Input: 

```
tccli wedata ListAssetViewsV2 --cli-unfold-argument  \
    --WorkspaceId 17677923090575947 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "tccatalog.v1.uid1876356801930330423@251436191_ap-guangzhou_CATALOG",
                    "AssetId": "tccatalog.v1.uid1876356801930330423",
                    "AssetName": "c4",
                    "AssetType": "CATALOG",
                    "CatalogContentType": "LAKEHOUSE",
                    "Comment": "test_comment222222test_commenttest_comdasdasd111",
                    "CreateTime": "1768028071625",
                    "FullName": "c4",
                    "Properties": [],
                    "WorkspaceId": "17677923090575947",
                    "WorkspacePath": ""
                }
            ],
            "NextPageToken": "eyJzZWFyY2hBZnRlclZhbHVlcyI6WzE3NjgwMjgwNzE2MjUsInRjY2F0YWxvZy52MS51aWQxODc2MzU2ODAxOTMwMzMwNDIzQDI1MTQzNjE5MV9hcC1ndWFuZ3pob3VfQ0FUQUxPRyJdfQ=="
        },
        "RequestId": "2b2e1af4-1e6a-49f2-a980-1ea3b1d10b2b"
    }
}
```

