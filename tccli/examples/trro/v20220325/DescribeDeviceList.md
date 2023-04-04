**Example 1: 设备列表获取示例**



Input: 

```
tccli trro DescribeDeviceList --cli-unfold-argument  \
    --ProjectId f3glr49rc96pralw \
    --SearchWords xx \
    --DeviceType field
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
                "DeviceName": "test1",
                "ProjectId": "xx",
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

