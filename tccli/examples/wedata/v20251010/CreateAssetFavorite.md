**Example 1: 收藏Catalog**

收藏Catalog

Input: 

```
tccli wedata CreateAssetFavorite --cli-unfold-argument  \
    --AssetType CATALOG \
    --AssetGuid DataLakeCatalogId \
    --FullName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "87d7c674-d976-4b4b-821f-4175e20ba298"
    }
}
```

**Example 2: 收藏表**

收藏表

Input: 

```
tccli wedata CreateAssetFavorite --cli-unfold-argument  \
    --AssetType TABLE \
    --AssetGuid tb8 \
    --FullName c.s.tb8
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "b9c8a24c-472d-4427-9dd4-10c0a18c1802"
    }
}
```

**Example 3: 新增模型收藏**

新增模型收藏

Input: 

```
tccli wedata CreateAssetFavorite --cli-unfold-argument  \
    --AssetType MODEL \
    --AssetGuid md1 \
    --FullName c.s.md1
```

Output: 
```
{
    "Response": {
        "RequestId": "a03117b6-2281-4bfe-80ea-a3c8e907cc0d",
        "Data": {
            "Result": true
        }
    }
}
```

