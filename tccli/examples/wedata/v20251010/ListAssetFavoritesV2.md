**Example 1: 我的收藏列表**

我的收藏列表

Input: 

```
tccli wedata ListAssetFavoritesV2 --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --AssetTypes DASHBOARD \
    --Detailed True \
    --MaxResults 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "796417389660397568@251436191_ap-guangzhou_DASHBOARD",
                    "AssetId": "796417389660397568",
                    "AssetName": "New Dashboard 2026-01-06 16:38:18",
                    "AssetType": "DASHBOARD",
                    "CatalogContentType": "",
                    "Comment": "",
                    "CreateTime": "1767768174421",
                    "FullName": "",
                    "Properties": [
                        {
                            "Key": "DisplayName",
                            "Value": "New Dashboard 2026-01-06 16:38:18"
                        }
                    ],
                    "WorkspaceId": "17622177773248536"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "952fcea1-d4bb-4b1e-801b-6a11afee6200"
    }
}
```

