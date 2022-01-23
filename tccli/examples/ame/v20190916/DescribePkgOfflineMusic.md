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
                "ItemId": "ABCD",
                "MusicName": "A",
                "OffRemark": "授权到期",
                "OffTime": "2006-01-01 00:00:00"
            }
        ],
        "RequestId": "xxx",
        "TotalCount": 1
    }
}
```

