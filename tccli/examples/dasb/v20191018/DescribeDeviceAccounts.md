**Example 1: 查询主机账号列表**

查询主机账号列表

Input: 

```
tccli dasb DescribeDeviceAccounts --cli-unfold-argument  \
    --DeviceId 1 \
    --Account root
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "79b7b771-368d-44b7-b954-f0cceda748e2",
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

