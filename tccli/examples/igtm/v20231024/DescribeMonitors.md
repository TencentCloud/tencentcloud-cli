**Example 1: 获取所有监控器**

获取所有监控器

Input: 

```
tccli igtm DescribeMonitors --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MonitorDataSet": [
            {
                "MonitorId": 1,
                "MonitorName": "测试监控器",
                "Uin": "10012894645",
                "DetectorGroupIds": [
                    1
                ],
                "CheckProtocol": "HTTP",
                "CheckInterval": 1,
                "PingNum": 1,
                "TcpPort": 1,
                "Host": "igtmtest.com",
                "Path": "/path",
                "ReturnCodeThreshold": 1,
                "EnableRedirect": "DISABLED",
                "EnableSni": "DISABLED",
                "PacketLossRate": 50,
                "Timeout": 15,
                "FailTimes": 4,
                "FailRate": 100,
                "CreatedOn": "2025-02-25 20:24:49",
                "UpdatedOn": "2025-02-25 20:24:49",
                "DetectorStyle": "INTERNAL",
                "DetectNum": 0,
                "ContinuePeriod": 1
            }
        ],
        "RequestId": "398db591-8793-4a0f-aaa3-3a0131494184"
    }
}
```

