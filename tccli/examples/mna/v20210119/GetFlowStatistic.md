**Example 1: 获取指定id设备流量使用信息**

获取指定id设备流量使用信息

Input: 

```
tccli mna GetFlowStatistic --cli-unfold-argument  \
    --EndTime 1659514692 \
    --Type 1 \
    --DeviceId mna-dev1 \
    --TimeGranularity 1 \
    --BeginTime 1659513692
```

Output: 
```
{
    "Response": {
        "MaxValue": 51548,
        "AvgValue": 15441,
        "TotalValue": 656546,
        "NetDetails": [
            {
                "Time": "1659513692",
                "Current": 3546545
            },
            {
                "Time": "1659513692",
                "Current": 4454864
            },
            {
                "Time": "1659513692",
                "Current": 4848941
            }
        ],
        "RequestId": ""
    }
}
```

**Example 2: 获取多个设备的流量使用信息之和**



Input: 

```
tccli mna GetFlowStatistic --cli-unfold-argument  \
    --EndTime 1659514692 \
    --Type 1 \
    --DeviceId  \
    --DeviceList mna-dev1 mna-dev2 \
    --TimeGranularity 1 \
    --BeginTime 1659513692
```

Output: 
```
{
    "Response": {
        "MaxValue": 51548,
        "AvgValue": 15441,
        "TotalValue": 656546,
        "NetDetails": [
            {
                "Time": "1659513692",
                "Current": 3546545
            },
            {
                "Time": "1659513692",
                "Current": 4454864
            },
            {
                "Time": "1659513692",
                "Current": 4848941
            }
        ],
        "RequestId": ""
    }
}
```

