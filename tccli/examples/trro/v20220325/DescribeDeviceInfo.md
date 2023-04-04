**Example 1: 获取设备信息示例**



Input: 

```
tccli trro DescribeDeviceInfo --cli-unfold-argument  \
    --ProjectId f3glr49ry0i0xlm7 \
    --DeviceId test1
```

Output: 
```
{
    "Response": {
        "DeviceName": "test device1",
        "LastReportTime": "2022-03-22T09:00:00+08:00",
        "DeviceStatus": "offline",
        "DeviceType": "field",
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "ModifyTime": "2022-03-22T08:00:00+08:00"
    }
}
```

