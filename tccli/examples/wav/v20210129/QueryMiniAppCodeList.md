**Example 1: 查询小程序码列表**



Input: 

```
tccli wav QueryMiniAppCodeList --cli-unfold-argument  \
    --Cursor +1H24tK0tELjSiTOR10DzA \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NextCursor": "+1H24tK0tELjSiTOR10DzA==",
        "PageData": [
            {
                "MiniAdminUrl": "https://weworksaas-web-dev.map.qq.com/",
                "State": 1,
                "CreateTime": 1618556502,
                "UpdateTime": 1618556507,
                "MiniAppName": "官方小程序",
                "MiniAppLogo": "https://tmap-travel-didi-1255598736.cos.ap-guangzhou.myqcloud.com/media/9b2bfb85-9d3a-41d2-a6cb-2ac95b11af68.jpg",
                "Id": 10
            }
        ],
        "RequestId": "4d48312c-a062-4875-a5d5-69f0f11baf96"
    }
}
```

