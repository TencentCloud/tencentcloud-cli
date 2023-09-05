**Example 1: 应用列表**

获取应用列表

Input: 

```
tccli weilingwith DescribeApplicationList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 3 \
    --ApplicationToken XggJvayJyusfUwuoJ2OlT4Z2YAVq6bVo
```

Output: 
```
{
    "Response": {
        "RequestId": "2ebee73c-8477-48c0-ad4d-8a748b7842a3",
        "Result": {
            "ApplicationInfoList": [
                {
                    "Address": "http://checkproject-a6f6718d.dtwin.tencent.com/testcodingpush",
                    "ApplicationId": "10041",
                    "ApplicationLogo": {
                        "FileId": "359cc1b5-88c1-4dd6-8ff4-21d0b36ac7e2",
                        "Url": "https://wetwin-manager-1258344699.cos.ap-guangzhou.myqcloud.com/%2F100055/0/20230717/359cc1b5-88c1-4dd6-8ff4-21d0b36ac7e2/%E8%B5%84%E4%BA%A7%E7%AE%A1%E7%90%86-%E9%BB%91.png?q-sign-algorithm=sha1&q-ak=AKIDiFWWFo67rLZXFgrlNinb8NL2SaR2M0OU&q-sign-time=1693452005%3B1693453205&q-key-time=1693452005%3B1693453205&q-header-list=host&q-url-param-list=&q-signature=6bf531d1b08d6f75eb7e153c24746a61d7be37d0"
                    },
                    "Description": "12345611111",
                    "EnglishName": "zctest1111",
                    "Name": "智能资产管理",
                    "Type": 0
                },
                {
                    "Address": "http://t-ws.twins.tencent.com/proxy/29098b25-447d-437e-987a-d493d55e84f5/weiling-pubsub/test",
                    "ApplicationId": "10048",
                    "ApplicationLogo": {
                        "FileId": "",
                        "Url": ""
                    },
                    "Description": "",
                    "EnglishName": "MsgCenter",
                    "Name": "消息服务",
                    "Type": 0
                },
                {
                    "Address": "http://t.twins.tencent.com/",
                    "ApplicationId": "10051",
                    "ApplicationLogo": {
                        "FileId": "",
                        "Url": ""
                    },
                    "Description": "",
                    "EnglishName": "IOT",
                    "Name": "孪生中台(物联感知中心)",
                    "Type": 0
                }
            ],
            "TotalCount": "171"
        }
    }
}
```

