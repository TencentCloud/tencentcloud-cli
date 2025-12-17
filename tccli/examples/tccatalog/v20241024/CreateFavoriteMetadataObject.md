**Example 1: 收藏元数据对象**



Input: 

```
tccli tccatalog CreateFavoriteMetadataObject --cli-unfold-argument  \
    --FullName test.test.test1 \
    --Type volume
```

Output: 
```
{
    "Response": {
        "FavoriteMetadataObject": {
            "CreatedTime": "2024-12-17 17:43:37",
            "FullName": "test.test.test1",
            "Type": "volume"
        },
        "RequestId": "220d919a-12ff-429d-9030-99a8a1dfa942"
    }
}
```

