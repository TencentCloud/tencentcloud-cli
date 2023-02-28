**Example 1: 查询主机账号列表**

查询主机账号列表

Input: 

```
tccli dasb DescribeDeviceAccounts --cli-unfold-argument  \
    --DeviceId 1 \
    --Account xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "DeviceAccountSet": [
            {
                "BoundPrivateKey": true,
                "Account": "xx",
                "Id": 1,
                "BoundPassword": true,
                "DeviceId": 1
            }
        ]
    }
}
```

