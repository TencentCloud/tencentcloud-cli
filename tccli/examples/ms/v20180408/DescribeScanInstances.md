**Example 1: 查询扫描实例列表**

根据提交实例的包名和名称进行筛选，并返回最新的20条记录

Input: 

```
tccli ms DescribeScanInstances --cli-unfold-argument  \
    --Filters.0.Name AppName\
    --Filters.0.Value wechat\
    --Filters.1.Name AppPkgName\
    --Filters.1.Value com.tencent.mm\
    --Offset 0\
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "TotalCount": 1,
        "ScanSet": [
            {
                "ItemId": "1234-xcse-ddw1",
                "AppName": "微信",
                "AppPkgName": "com.tencent.mm",
                "AppVersion": "6.5",
                "AppMd5": "der2331ds",
                "AppSize": 123454,
                "TaskTime": 1524744997,
                "AppSid": "wiqhiqxasqx282787",
                "ScanCode": 0,
                "AppIconUrl": "https://wwww.example.com/12334",
                "TaskStatus": 1
            }
        ]
    }
}
```

