**Example 1: 根据DeviceName（testdev）获取流量监控信息**



Input: 

```
tccli mna GetNetMonitorByName --cli-unfold-argument  \
    --DeviceName testdev \
    --BeginTime 1758545194 \
    --EndTime 1758545494 \
    --Metrics RxRate
```

Output: 
```
{
    "Response": {
        "AccessRegion": "MC",
        "MonitorData": [
            {
                "BusinessMetrics": 158.133333,
                "SlotNetInfo": [
                    {
                        "Current": 7104.8,
                        "NetInfoName": "rmnet_data5",
                        "PublicIP": "123.138.183.224:34771"
                    },
                    {
                        "Current": 7331.466667,
                        "NetInfoName": "wlan0",
                        "PublicIP": "113.142.183.133:37034"
                    }
                ],
                "Time": "1758545160"
            },
            {
                "BusinessMetrics": 1329.733333,
                "SlotNetInfo": [
                    {
                        "Current": 7064.666667,
                        "NetInfoName": "rmnet_data5",
                        "PublicIP": "123.138.183.224:34771"
                    },
                    {
                        "Current": 8696.8,
                        "NetInfoName": "wlan0",
                        "PublicIP": "113.142.183.133:37034"
                    }
                ],
                "Time": "1758545220"
            },
            {
                "BusinessMetrics": 497.466667,
                "SlotNetInfo": [
                    {
                        "Current": 7428.4,
                        "NetInfoName": "rmnet_data5",
                        "PublicIP": "123.138.183.224:34771"
                    },
                    {
                        "Current": 7513.066667,
                        "NetInfoName": "wlan0",
                        "PublicIP": "113.142.183.133:37034"
                    }
                ],
                "Time": "1758545280"
            },
            {
                "BusinessMetrics": 1156.933333,
                "SlotNetInfo": [
                    {
                        "Current": 9330.933333,
                        "NetInfoName": "rmnet_data5",
                        "PublicIP": "123.138.183.224:34771"
                    },
                    {
                        "Current": 8388.133333,
                        "NetInfoName": "wlan0",
                        "PublicIP": "113.142.183.133:37034"
                    }
                ],
                "Time": "1758545340"
            },
            {
                "BusinessMetrics": 3181.866667,
                "SlotNetInfo": [
                    {
                        "Current": 8754,
                        "NetInfoName": "rmnet_data5",
                        "PublicIP": "123.138.183.224:34771"
                    },
                    {
                        "Current": 9718.666667,
                        "NetInfoName": "wlan0",
                        "PublicIP": "113.142.183.133:37034"
                    }
                ],
                "Time": "1758545400"
            },
            {
                "BusinessMetrics": -1,
                "SlotNetInfo": [
                    {
                        "Current": -1,
                        "NetInfoName": "rmnet_data5",
                        "PublicIP": "123.138.183.224:34771"
                    },
                    {
                        "Current": -1,
                        "NetInfoName": "wlan0",
                        "PublicIP": "113.142.183.133:37034"
                    }
                ],
                "Time": "1758545460"
            }
        ],
        "RequestId": "09975f22-b4fc-45a6-81d4-67236cb9e867"
    }
}
```

