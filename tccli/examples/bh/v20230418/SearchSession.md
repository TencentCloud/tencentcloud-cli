**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli bh SearchSession --cli-unfold-argument  \
    --UserName zhangsan \
    --Account admistrator \
    --PrivateIp 127.0.0.1 \
    --PublicIp 192.168.12.12 \
    --FromIp 192.12.12.12 \
    --StartTime 2020-12-20T19:51:23+08:00 \
    --EndTime 2020-12-30T19:51:23+08:00 \
    --Kind 1 \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082",
        "SessionSet": [
            {
                "UserName": "John",
                "DeviceName": "MobileDevice",
                "Account": "john***@example.com",
                "Protocol": "HTTPS",
                "RealName": "John Doe",
                "Status": 1,
                "InstanceId": "Ins-bhtest",
                "FromIp": "192.168.0.1",
                "DangerCount": 1,
                "PublicIp": "203.0.113.1",
                "Count": 1,
                "StartTime": "2022-01-01 10:00:00",
                "ApCode": "ABC123",
                "Duration": 3600.5,
                "PrivateIp": "10.0.0.1",
                "EndTime": "2022-01-01 11:00:00",
                "Id": "session-1a2b3c",
                "Size": 1024
            }
        ]
    }
}
```

