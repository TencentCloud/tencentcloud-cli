**Example 1: 批量删除设备示例**



Input: 

```
tccli trro BatchDeleteDevices --cli-unfold-argument  \
    --ProjectId f3glr49ry0i0xlm7 \
    --DeviceIds dev1 dev2
```

Output: 
```
{
    "Response": {
        "FailedDeviceIds": [],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

