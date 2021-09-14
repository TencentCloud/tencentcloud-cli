**Example 1: 查询歌曲在售状态**

根据音乐信息查询音乐是否在售

Input: 

```
tccli ame DescribeMusicSaleStatus --cli-unfold-argument  \
    --PurchaseType 1 \
    --MusicIds xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "MusicStatusSet": [
            {
                "MusicId": "xx",
                "SaleStatus": 0
            }
        ]
    }
}
```

