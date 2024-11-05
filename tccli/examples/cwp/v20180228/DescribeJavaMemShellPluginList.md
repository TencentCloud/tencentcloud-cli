**Example 1: 查询java内存马插件列表**

查询java内存马插件列表

Input: 

```
tccli cwp DescribeJavaMemShellPluginList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Uuid": "d4cc302e-09e5-436f-b99b-5ab9c9070323",
                "Quuid": "d4cc302e-09e5-436f-b99b-5ab9c9070323",
                "Alias": "安全中心x主机自动化机器",
                "HostIp": "10.0.1.92",
                "JavaShellStatus": 1,
                "Exception": 0,
                "CreateTime": "2024-09-06 15:55:30",
                "ModifyTime": "2024-09-06 15:55:30",
                "MachineExtraInfo": {
                    "WanIP": "119.29.132.142",
                    "PrivateIP": "10.10.0.16",
                    "NetworkType": 0,
                    "NetworkName": "vpc-d7f***",
                    "InstanceID": "ins-elxffb4w",
                    "HostName": "hn***"
                }
            }
        ],
        "RequestId": "ec3bf9d4-5305-45cb-ba1c-7ba0811a2dc7",
        "TotalCount": 1
    }
}
```

