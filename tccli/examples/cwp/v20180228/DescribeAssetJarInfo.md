**Example 1: 获取Jar包详情**



Input: 

```
tccli cwp DescribeAssetJarInfo --cli-unfold-argument  \
    --Quuid xx \
    --Uuid xx \
    --Id xx
```

Output: 
```
{
    "Response": {
        "Jar": {
            "Status": 1,
            "OsInfo": "xx",
            "UpdateTime": "xx",
            "Name": "xx",
            "Process": [
                {
                    "Status": "xx",
                    "Name": "xx",
                    "Version": "xx",
                    "User": "xx",
                    "StartTime": "xx",
                    "Path": "xx"
                }
            ],
            "MachineName": "xx",
            "Version": "xx",
            "Path": "xx",
            "Type": 1,
            "MachineIp": "xx",
            "Md5": "xx"
        },
        "RequestId": "xx"
    }
}
```

