**Example 1: 获取某个用户的加固资源信息**

获取某个用户的加固资源信息

Input: 

```
tccli ms DescribeResourceInstances --cli-unfold-argument  \
    --Pids 12750 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "TotalCount": 10,
        "ResourceSet": [
            {
                "ResourceId": "",
                "ResourceName": "应用加固",
                "Pid": "",
                "CreateTime": "",
                "ExpireTime": "",
                "IsBind": 1,
                "BindInfo": {
                    "AppIcon": "",
                    "AppName": "微信",
                    "AppPkgName": "com.tencent.mm"
                }
            }
        ]
    }
}
```

