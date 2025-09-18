**Example 1: 导出IP溯源日志原始数据**

只返回IP和访问时间

Input: 

```
tccli es ExportIpTraceLog --cli-unfold-argument  \
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
        "IpTraceList": [
            {
                "NodeIp": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Timestamp": 171939488883
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

