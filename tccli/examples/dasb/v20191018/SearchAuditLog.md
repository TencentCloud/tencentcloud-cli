**Example 1: 搜索审计日志**

搜索审计日志

Input: 

```
tccli dasb SearchAuditLog --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+08:00 \
    --EndTime 2020-09-29T00:00:00+08:00 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AuditLogSet": [
            {
                "Sid": "qwedssdf",
                "Uin": "15546822843",
                "Time": "2020-09-27T00:00:00+08:00",
                "ClientIp": "10.15.35.41",
                "Operation": 5,
                "InstanceId": "ins-tearwsasd",
                "DeviceName": "readaoe",
                "Protocol": "SSH",
                "PrivateIp": "172.45.35.62",
                "PublicIp": "192.46.36.85",
                "SubAccountUin": "15847269574"
            }
        ],
        "TotalCount": 1,
        "RequestId": "1d3ef406-46bd-4770-8f0b-dbd4ac3d886e"
    }
}
```

