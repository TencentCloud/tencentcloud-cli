**Example 1: 查询扫描实例列表**

根据提交实例的包名和名称进行筛选，并返回最新的20条记录

Input: 

```
tccli ms DescribeScanInstances --cli-unfold-argument  \
    --Limit 20 \
    --Filters.0.Name AppPkgName \
    --Filters.0.Value com.tencent.mm \
    --Filters.1.Name AppName \
    --Filters.1.Value wechat \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ScanSet": [
            {
                "ItemId": "xx",
                "AppMd5": "xx",
                "AppName": "xx",
                "ScanCode": 1,
                "AppVersion": "xx",
                "TaskStatus": 1,
                "AppSid": "xx",
                "TaskTime": 1,
                "VulCount": 1,
                "AppSize": 1,
                "AppPkgName": "xx",
                "AppIconUrl": "xx",
                "SafeType": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

