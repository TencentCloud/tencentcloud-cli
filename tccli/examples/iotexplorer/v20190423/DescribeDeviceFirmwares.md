**Example 1: 获取设备固件信息**



Input: 

```
tccli iotexplorer DescribeDeviceFirmwares --cli-unfold-argument  \
    --ProductId xx \
    --DeviceName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "ef9ec631-7337-481b-a6c3-59a34b5f8502",
        "Firmwares": [
            {
                "UpdateTime": 1653893719,
                "FwType": "mcu",
                "Version": "mm_3.0"
            },
            {
                "UpdateTime": 1653893651,
                "FwType": "module",
                "Version": "module_v1.0.3"
            }
        ]
    }
}
```

