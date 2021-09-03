**Example 1: 直接绑定设备**



Input: 

```
tccli iotexplorer DirectBindDeviceInFamily --cli-unfold-argument  \
    --IotAppID ABCDE12345 \
    --UserID dev_49 \
    --FamilyId 0 \
    --ProductId 1 \
    --DeviceName tt \
    --RoomId 1
```

Output: 
```
{
    "Response": {
        "AppDeviceInfo": {
            "DeviceId": "FPEU28BCGP/dev1",
            "ProductId": "FPEU28BCGP",
            "DeviceName": "dev1",
            "AliasName": "t1",
            "IconUrl": "",
            "FamilyId": "f_cc67fefbcefd43d88a5c0157ee18c975",
            "RoomId": "0",
            "DeviceType": 0,
            "CreateTime": 1630310068,
            "UpdateTime": 1630310068
        },
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
    }
}
```

