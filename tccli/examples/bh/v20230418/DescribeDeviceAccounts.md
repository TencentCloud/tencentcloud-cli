**Example 1: 查询主机账号列表**

查询主机账号列表

Input: 

```
tccli bh DescribeDeviceAccounts --cli-unfold-argument  \
    --DeviceId 1 \
    --Account root
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082",
        "DeviceAccountSet": [
            {
                "BoundPrivateKey": true,
                "Account": "root",
                "Id": 1,
                "BoundPassword": true,
                "DeviceId": 1
            }
        ]
    }
}
```

