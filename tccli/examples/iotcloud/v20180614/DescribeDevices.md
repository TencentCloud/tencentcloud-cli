**Example 1: 获取设备列表**



Input: 

```
tccli iotcloud DescribeDevices --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --Offset 0 \
    --Limit 10 \
    --FirmwareVersion 1.0.0
```

Output: 
```
{
    "Response": {
        "Devices": [
            {
                "Tags": [
                    {
                        "Tag": "category",
                        "Type": 2,
                        "Value": "hello"
                    },
                    {
                        "Tag": "note",
                        "Type": 2,
                        "Value": ""
                    }
                ],
                "DeviceName": "test",
                "DeviceCert": "",
                "Online": 0,
                "ConnIP": 0,
                "LoginTime": 0,
                "Version": "1.0.0",
                "LastUpdateTime": 0,
                "DevicePsk": "",
                "DeviceType": 0,
                "Imei": "",
                "Isp": 0,
                "NbiotDeviceID": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "c81cf0fd-18bd-4f7a-845e-4f852645de2b"
    }
}
```

