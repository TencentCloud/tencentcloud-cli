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
            "MonitorName": "测试监控器",
            "Uin": "10012894645",
            "DetectorGroupIds": [
                1
            ],
            "CheckProtocol": "HTTP",
            "CheckInterval": 300,
            "PingNum": 20,
            "TcpPort": 80,
            "Host": "gtmtest.com",
            "Path": "/path",
            "ReturnCodeThreshold": 500,
            "EnableRedirect": "DISABLED",
            "EnableSni": "DISABLED",
            "PacketLossRate": 50,
            "Timeout": 15,
            "FailTimes": 1,
            "FailRate": 100,
            "CreatedOn": "2023-01-1 11:11:11",
            "UpdatedOn": "2023-01-1 11:11:11",
            "DetectorStyle": "INTERNAL",
            "DetectNum": 0,
            "ContinuePeriod": 1
        },
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

