**Example 1: 曲库包获取已核销歌曲回退数据**

根据购买曲库包用户可查询已回退的歌曲信息

Input: 

```
tccli ame DescribePkgOfflineMusic --cli-unfold-argument  \
    --PackageOrderId xx \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "OfflineMusicSet": [
            {
                "ItemId": "xx",
                "MusicName": "xx",
                "OffRemark": "xx",
                "OffTime": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalCount": 0
    }
}
```

