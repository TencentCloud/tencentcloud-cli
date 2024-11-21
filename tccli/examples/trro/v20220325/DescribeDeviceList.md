**Example 1: 设备列表获取示例**



Input: 

```
tccli trro DescribeDeviceList --cli-unfold-argument  \
    --ProjectId f3glr49r3axn0fu2 \
    --DeviceType field \
    --SearchWords dev1 \
    --PageSize 10 \
    --PageNumber 1 \
    --DeviceStatus offline
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Num": 1,
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "Devices": [
            {
                "DeviceName": "key",
                "ProjectId": "f3glr49r3axn0fu2",
                "LastReportTime": "2022-03-22T08:00:00+08:00",
                "DeviceStatus": "offline",
                "DeviceType": "field",
                "DeviceId": "dev1",
                "ModifyTime": "2022-03-21T08:00:00+08:00"
            }
        ]
    }
}
```

