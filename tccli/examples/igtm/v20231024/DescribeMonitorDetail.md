**Example 1:  查询监控器详情**

查询监控器详情

Input: 

```
tccli igtm DescribeMonitorDetail --cli-unfold-argument  \
    --MonitorId 1
```

Output: 
```
{
    "Response": {
        "MonitorDetail": {
            "MonitorId": 1,
            "MonitorName": "abc",
            "Uin": "abc",
            "DetectorGroupIds": [
                1
            ],
            "CheckProtocol": "abc",
            "CheckInterval": 1,
            "PingNum": 1,
            "TcpPort": 1,
            "Host": "abc",
            "Path": "abc",
            "ReturnCodeThreshold": 1,
            "EnableRedirect": "abc",
            "EnableSni": "abc",
            "PacketLossRate": 1,
            "Timeout": 1,
            "FailTimes": 1,
            "FailRate": 1,
            "DetectorStyle": "abc"
        },
        "RequestId": "xxx"
    }
}
```

