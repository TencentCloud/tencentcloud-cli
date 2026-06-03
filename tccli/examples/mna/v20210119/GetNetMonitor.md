**Example 1: 查询设备指定时间段下行速率**



Input: 

```
tccli mna GetNetMonitor --cli-unfold-argument  \
    --DeviceId mna-yujpsea3v0 \
    --BeginTime 1776346200 \
    --EndTime 1776346500 \
    --Metrics RxRate
```

Output: 
```
{
    "Response": {
        "AccessRegion": "MC",
        "MonitorData": [
            {
                "BusinessMetrics": 262585.6,
                "SlotNetInfo": [
                    {
                        "Current": 285197.866667,
                        "NetInfoName": "eth1",
                        "PublicIP": "115.227.8.235:19991"
                    }
                ],
                "Time": "1776346200"
            }
        ],
        "RequestId": "ceb36604-8a38-4147-8cd8-89d905facf52"
    }
}
```

