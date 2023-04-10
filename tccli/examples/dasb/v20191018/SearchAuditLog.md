**Example 1: 搜索审计日志**

搜索审计日志

Input: 

```
tccli dasb SearchAuditLog --cli-unfold-argument  \
    --StartTime 2020-01-01T01:01:01Z \
    --EndTime 2020-01-01T01:01:01Z
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AuditLogSet": [
            {
                "SubAccountUin": "xx",
                "DeviceName": "xx",
                "Protocol": "xx",
                "InstanceId": "xx",
                "Sid": "xx",
                "Uin": "xx",
                "PublicIp": "xx",
                "Time": "xx",
                "Operation": 1,
                "PrivateIp": "xx",
                "ClientIp": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

