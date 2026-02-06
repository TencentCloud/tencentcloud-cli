**Example 1: 获取发布渠道列表**



Input: 

```
tccli lke ListChannel --cli-unfold-argument  \
    --AppBizId 1927296561029113536 \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "ListChannel": [
            {
                "ChannelId": "1932046222365083648",
                "ChannelName": "微信服务号",
                "ChannelStatus": 2,
                "ChannelType": 10000,
                "Comment": "",
                "CreateTime": "1749470703",
                "UpdateTime": "1749470703",
                "UpdatedUser": "channel@qq.com",
                "YuanQiInfo": {
                    "VisibleRange": "share"
                }
            }
        ],
        "RequestId": "bf251d0d-0409-4849-98e7-81fd7dbcc994",
        "Total": 1
    }
}
```

