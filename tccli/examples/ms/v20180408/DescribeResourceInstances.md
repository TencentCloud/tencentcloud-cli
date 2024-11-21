**Example 1: 获取某个用户的加固资源信息**

获取某个用户的加固资源信息

Input: 

```
tccli ms DescribeResourceInstances --cli-unfold-argument  \
    --Pids 12750 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "svmsref_xxxxx",
        "ResourceSet": [
            {
                "ResourceId": "svmsref_xxxxx",
                "Pid": 1,
                "ExpireTime": 1,
                "IsBind": 1,
                "ResourceName": "资源名称",
                "BindInfo": {
                    "AppPkgName": "com.tencent.demo",
                    "AppIconUrl": "https://appicon,url.com/appicon",
                    "AppName": "AppName"
                },
                "CreateTime": 1
            }
        ]
    }
}
```

