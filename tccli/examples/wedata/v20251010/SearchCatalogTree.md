**Example 1: 搜索目录树**

搜索目录树

Input: 

```
tccli wedata SearchCatalogTree --cli-unfold-argument  \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "",
                    "AssetName": "tsing_catalog",
                    "AssetType": "CATALOG",
                    "CatalogContentType": "TABLE",
                    "ChildNodes": [
                        {
                            "AssetGuid": "",
                            "AssetName": "default",
                            "AssetType": "SCHEMA",
                            "CatalogContentType": "TABLE",
                            "ChildNodes": [],
                            "Comment": "Default database for catalog tsing_catalog",
                            "CreateTime": "1764760675268",
                            "FullName": "tsing_catalog.default",
                            "IsFavorite": false
                        }
                    ],
                    "Comment": "tsing_catalog111",
                    "CreateTime": "1762605465451",
                    "FullName": "tsing_catalog",
                    "IsFavorite": false
                }
            ],
            "NextPageToken": "{\"offset\":2,\"pageSize\":200,\"isEnd\":false}"
        },
        "RequestId": "a5f874a1-4ee2-4dec-bb9d-f5efb5547b2f"
    }
}
```

