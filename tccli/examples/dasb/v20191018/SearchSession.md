**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli dasb SearchSession --cli-unfold-argument  \
    --UserName user1 \
    --Account admistrator \
    --PrivateIp 127.0.0.1 \
    --PublicIp 192.168.12.12 \
    --FromIp 192.12.12.12 \
    --StartTime 2020-01-02T01:01:01Z \
    --EndTime 2020-01-02T01:02:00Z \
    --Kind 1 \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "SessionSet": [
            {
                "UserName": "xx",
                "DeviceName": "xx",
                "Account": "xx",
                "Protocol": "xx",
                "RealName": "xx",
                "Status": 1,
                "InstanceId": "xx",
                "FromIp": "xx",
                "DangerCount": 1,
                "PublicIp": "xx",
                "Count": 1,
                "StartTime": "xx",
                "ApCode": "xx",
                "Duration": 0.0,
                "PrivateIp": "xx",
                "EndTime": "xx",
                "Id": "xx",
                "Size": 1
            }
        ]
    }
}
```

