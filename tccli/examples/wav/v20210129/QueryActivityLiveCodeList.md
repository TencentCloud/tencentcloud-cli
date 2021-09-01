**Example 1: 查询活码列表**



Input: 

```
tccli wav QueryActivityLiveCodeList --cli-unfold-argument  \
    --Cursor eKMXI/XqG5yQmGrx3qXBRrthr/F8JGlknuYJTKHZaks \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NextCursor": "eKMXI/XqG5yQmGrx3qXBRrthr/F8JGlknuYJTKHZaks=",
        "PageData": [
            {
                "LiveCodePreview": "https://tmap-travel-didi-1255598736.cos.ap-guangzhou.myqcloud.com/liveCode/ww81084a80e7663baf/1405537314006573058.jpg",
                "ActivityName": "10日券",
                "ActivityId": 1405537288119328800,
                "CreateTime": 1623941184,
                "ShortChainAddress": "https://aggretrip.map.qq.com/wework_saas/dist/index.html?wexin_target=weixin%3A%2F%2Fdl%2Fbusiness%2F%3Ft%3DreO6Co5q6ko",
                "UpdateTime": 1623941184,
                "LiveCodeData": "",
                "LiveCodeState": 0,
                "LiveCodeName": "22",
                "LiveCodeId": 1405537311796174800
            }
        ],
        "RequestId": "e520d8eb-969f-4554-bf5f-169b344935e8"
    }
}
```

