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
                "CreatedOn": "abc",
                "UpdatedOn": "abc",
                "DetectorStyle": "abc"
            }
        ],
        "RequestId": "398db591-8793-4a0f-aaa3-3a0131494184"
    }
}
```

