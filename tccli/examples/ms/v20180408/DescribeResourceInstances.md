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
        "RequestId": "xx",
        "ResourceSet": [
            {
                "ResourceId": "xx",
                "Pid": 1,
                "ExpireTime": 1,
                "IsBind": 1,
                "ResourceName": "xx",
                "BindInfo": {
                    "AppPkgName": "xx",
                    "AppIconUrl": "xx",
                    "AppName": "xx"
                },
                "CreateTime": 1
            }
        ]
    }
}
```

