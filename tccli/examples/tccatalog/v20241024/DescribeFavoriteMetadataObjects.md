**Example 1: 获取100个收藏的元数据对象**



Input: 

```
tccli tccatalog DescribeFavoriteMetadataObjects --cli-unfold-argument  \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "RequestId": "a935b6b6-2dae-4bfd-a88c-eaccec55e284",
        "FavoriteMetadataObjects": [
            {
                "FullName": "test_mysql",
                "Type": "catalog",
                "CreatedTime": "2024-12-17 15:53:08"
            }
        ]
    }
}
```

