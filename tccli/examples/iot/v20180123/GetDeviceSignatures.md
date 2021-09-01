**Example 1: 批量获取设备绑定签名**

获取设备绑定签名，用于用户绑定某个设备以便进行控制

Input: 

```
tccli iot GetDeviceSignatures --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceNames device1 device2
```

Output: 
```
{
    "Response": {
        "RequestId": "453702e4-61f1-4ed5-83c1-6f1a5b747751",
        "DeviceSignatures": [
            {
                "DeviceName": "device1",
                "DeviceSignature": "BSBm4CDokgjFPrwRwTGkbJarpKQ12fXXP8KhzBDyzhBYpVIx+QhT/rpMd0lUhKNR1LPa+kGCUuR5PypPc3v2ne6GB9sYw/rUEjp/tg=="
            },
            {
                "DeviceName": "device2",
                "DeviceSignature": "5lrbM6WwyGJwr2iEFDcW2yown2mvU/UpkfhCfx76A6/YfwXW14KVgKwHMDFfnGOvRVfdlWXFRMEbrLcbhgb58zjE7vruRNJ+HrggIA=="
            }
        ]
    }
}
```

