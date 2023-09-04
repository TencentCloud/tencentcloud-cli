**Example 1: 设备状态统计列表**

正常响应

Input: 

```
tccli weilingwith DescribeDeviceStatusStat --cli-unfold-argument  \
    --Level 1 \
    --WorkspaceId 1016 \
    --ApplicationToken YVySZSL1Lp5UtSJ5uJVLJYOKDEGfCCH2
```

Output: 
```
{
    "Response": {
        "RequestId": "503f6887-d9af-48b9-91cb-999644f45e63",
        "Result": {
            "DeviceTypeOverviewSet": [
                {
                    "DeviceType": "w0715010",
                    "Fault": 0,
                    "Name": "多功能网关",
                    "Normal": 6,
                    "Offline": 8212,
                    "Total": 8218
                }
            ],
            "FaultSum": 15,
            "NormalSum": 87,
            "OfflineSum": 8689,
            "StatLevelSet": [],
            "Total": 8791,
            "WorkspaceId": 1016
        }
    }
}
```

