**Example 1: 成功示例**



Input: 

```
tccli iotexplorer GetWechatDeviceTicket --cli-unfold-argument  \
    --ProductId 123wdc \
    --DeviceName d1
```

Output: 
```
{
    "Response": {
        "WXDeviceInfo": {
            "DeviceId": "II0Q47L8B9/e_70660037_1",
            "WXIoTDeviceInfo": {
                "SN": "II0Q47L8B9_e_70660037_1",
                "SNTicket": "1d07ea20caa8a12e1e1",
                "ModelId": "xd1Fje8YfY4aWw"
            }
        },
        "RequestId": "PGagP4JXp"
    }
}
```

