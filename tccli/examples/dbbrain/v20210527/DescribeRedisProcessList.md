**Example 1: 获取 Redis 实例 Proxy 实时会话详情列表**

指定 Offset 分页获取实例 Proxy 实时会话详情列表。

Input: 

```
tccli dbbrain DescribeRedisProcessList --cli-unfold-argument  \
    --InstanceId crs-qylqks3c \
    --Product redis \
    --Offset 50 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "8108c1c0-bbcc-11ec-adb9-eb9c1358e02b",
        "ProxyCount": 198,
        "Processes": [
            {
                "Address": "100.12.168.216:33064",
                "Age": 11788,
                "FileDescriptor": 3,
                "Id": -522451396107420,
                "Idle": 0,
                "LastCommand": "client",
                "Name": "",
                "ProxyId": "49c4c738a3398cb0a41914396e24db2dee29d1e3"
            },
            {
                "Address": "100.1.168.115:36938",
                "Age": 47,
                "FileDescriptor": 7,
                "Id": -803926372818076,
                "Idle": 47,
                "LastCommand": "command",
                "Name": "",
                "ProxyId": "49c4c538a3397cb0a41914796e24db3dee29d1e3"
            }
        ]
    }
}
```

