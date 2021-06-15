**Example 1: 查询小程序码列表**



Input: 

```
tccli wav QueryMiniAppCodeList --cli-unfold-argument  \
    --Cursor xxxx \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PageData": [
            {
                "MiniAdminUrl": "https://www.xxx.com",
                "State": 0,
                "CreateTime": 1621309668,
                "UpdateTime": 1621309668,
                "MiniAppName": "小程序",
                "MiniAppLogo": "https://xxx.jpg",
                "Id": 34
            }
        ],
        "NextCursor": "xx",
        "RequestId": "xx"
    }
}
```

