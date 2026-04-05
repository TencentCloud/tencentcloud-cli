**Example 1: 通过关键字查询收藏列表**

通过关键字查询收藏列表

Input: 

```
tccli wedata ListAssetFavorites --cli-unfold-argument  \
    --Keyword t1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": "10",
            "Items": [
                {
                    "AssetName": "t1",
                    "AssetType": "TABLE",
                    "Comment": "",
                    "CreateTime": "2025-10-29T14:17:53+08:00",
                    "FullName": "c.s.t1"
                }
            ]
        },
        "RequestId": "9ce60818-199f-4d46-ba8e-96af0039a8eb"
    }
}
```

