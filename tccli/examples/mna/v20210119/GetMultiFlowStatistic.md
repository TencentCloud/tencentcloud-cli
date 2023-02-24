**Example 1: 批量设备流量使用信息**

批量获取指定设备列表流量使用信息

Input: 

```
tccli mna GetMultiFlowStatistic --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FlowDetails": [
            {
                "AvgValue": 26524619322,
                "DeviceId": "mna-obzuio2pij",
                "MaxValue": 44183705788,
                "NetDetails": [
                    {
                        "Current": 421334,
                        "Time": "1675756800"
                    },
                    {
                        "Current": 32279199625,
                        "Time": "1675760400"
                    },
                    {
                        "Current": 44183705788,
                        "Time": "1675771200"
                    },
                    {
                        "Current": 29635150541,
                        "Time": "1675774800"
                    }
                ],
                "TotalValue": 106098477288
            },
            {
                "AvgValue": 31803650050.5,
                "DeviceId": "mna-ps9x7eako2",
                "MaxValue": 50892172491,
                "NetDetails": [
                    {
                        "Current": 22711,
                        "Time": "1675756800"
                    },
                    {
                        "Current": 46732569185,
                        "Time": "1675760400"
                    },
                    {
                        "Current": 29589835815,
                        "Time": "1675771200"
                    },
                    {
                        "Current": 50892172491,
                        "Time": "1675774800"
                    }
                ],
                "TotalValue": 127214600202
            }
        ],
        "RequestId": "ffad4f52-505f-4563-9431-b2ca1b5a887e"
    }
}
```

