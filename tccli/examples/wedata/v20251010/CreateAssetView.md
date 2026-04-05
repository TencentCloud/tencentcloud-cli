**Example 1: 增加模型浏览记录**

增加模型浏览记录

Input: 

```
tccli wedata CreateAssetView --cli-unfold-argument  \
    --AssetType MODEL \
    --AssetGuid md2 \
    --FullName c.s.md2
```

Output: 
```
{
    "Response": {
        "RequestId": "9910ef10-9fa4-4f5f-aabf-ce17a5e334c7",
        "Data": {
            "Result": true
        }
    }
}
```

**Example 2: 增加表浏览记录**

增加表浏览记录

Input: 

```
tccli wedata CreateAssetView --cli-unfold-argument  \
    --AssetType TABLE \
    --AssetGuid tb1 \
    --FullName c.s.tb1
```

Output: 
```
{
    "Response": {
        "RequestId": "33423851-af88-4d17-83d5-9ab094534973",
        "Data": {
            "Result": true
        }
    }
}
```

**Example 3: 收藏Catalog**

收藏Catalog

Input: 

```
tccli wedata CreateAssetView --cli-unfold-argument  \
    --AssetType CATALOG \
    --AssetGuid c1 \
    --FullName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "70bdfa45-4f3c-40d7-aa65-851ba3a54cf7"
    }
}
```

