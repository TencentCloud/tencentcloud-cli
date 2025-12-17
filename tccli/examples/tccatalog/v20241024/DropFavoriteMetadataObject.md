**Example 1: 取消原数据对象的收藏**



Input: 

```
tccli tccatalog DropFavoriteMetadataObject --cli-unfold-argument  \
    --FullName mysql_test
```

Output: 
```
{
    "Response": {
        "Dropped": true,
        "RequestId": "00f3864d-4ee9-401a-a1e7-d6985cb4802e"
    }
}
```

