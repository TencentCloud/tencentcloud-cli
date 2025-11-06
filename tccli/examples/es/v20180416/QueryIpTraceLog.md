**Example 1: 查询IP溯源日志**



Input: 

```
tccli es QueryIpTraceLog --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --StartTime 2024-08-11 12:00:00 \
    --EndTime 2024-08-11 12:10:00 \
    --Offset 1 \
    --Limit 100 \
    --RemoteIp 127.0.0.1 \
    --TraceType Request \
    --NetType Public \
    --ReqTypeOrRspStatus POST \
    --SearchKey idx-abc \
    --NodeIp 127.0.0.1
```

Output: 
```
{
    "Response": {
        "IpTraceLogList": [
            {
                "Timestamp": "",
                "RemoteIp": "127.0.0.1",
                "TraceType": "req",
                "NetType": "Public",
                "Message": "",
                "Uri": "message",
                "PublicIp": "null",
                "ReqTypeOrRspStatus": "",
                "NodeIp": "127.0.0.1"
            }
        ],
        "Total": 12,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

