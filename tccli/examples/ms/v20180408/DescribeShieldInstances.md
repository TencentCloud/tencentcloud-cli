**Example 1: 查询加固实例列表**

根据加固实例的包名和名称进行筛选，并返回最新的20条记录

Input: 

```
tccli ms DescribeShieldInstances --cli-unfold-argument  \
    --Filters.0.Name AppName \
    --Filters.0.Value wechat \
    --Filters.1.Name AppPkgName \
    --Filters.1.Value com.tencent.mm \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "TotalCount": 10,
        "AppSet": [
            {
                "ItemId": "1234-xcse-ddw1",
                "AppName": "微信",
                "AppPkgName": "com.tencent.mm",
                "AppVersion": "6.5",
                "AppMd5": "der2331ds",
                "AppSize": 123454,
                "ServiceEdition": "basic",
                "ShieldCode": 0,
                "AppUrl": "https://www.example.com/a.apk",
                "AppIconUrl": "https://wwww.example.com/12334",
                "ShieldMd5": "ae5df985a27b07f56d8c670fef70d7c9",
                "ShieldSize": 1193311,
                "TaskStatus": 1,
                "TaskTime": 1524744997
            }
        ]
    }
}
```

