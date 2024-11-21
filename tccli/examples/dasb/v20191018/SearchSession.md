**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli dasb SearchSession --cli-unfold-argument  \
    --UserName zhangsan \
    --Account admistrator \
    --PrivateIp 127.0.0.1 \
    --PublicIp 192.168.12.12 \
    --FromIp 192.12.12.12 \
    --StartTime 2020-12-20T19:51:23+08:00 \
    --EndTime 2020-12-20T20:51:23+08:00 \
    --Kind 1 \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SessionSet": [
            {
                "UserName": "zhangsan",
                "RealName": "张三",
                "Account": "root",
                "StartTime": "2020-12-20T19:51:23+08:00",
                "EndTime": "2020-12-21T19:51:23+08:00",
                "Size": 1,
                "InstanceId": "Ins-1jsa9",
                "DeviceName": "运维主机",
                "PrivateIp": "192.168.0.31",
                "PublicIp": "100.10.1.1",
                "FromIp": "1.1.1.1",
                "Duration": 0,
                "Count": 1,
                "DangerCount": 1,
                "Status": 1,
                "Id": "1",
                "ApCode": "ag-guangzhou",
                "Protocol": "SSH"
            }
        ],
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

