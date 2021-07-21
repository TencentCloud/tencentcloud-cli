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
        "TotalCount": 1,
        "RequestId": "xx",
        "Devices": [
            {
                "EnableState": 1,
                "LastOfflineTime": 1,
                "Version": "xx",
                "CertState": 1,
                "Online": 1,
                "FirmwareUpdateTime": 1,
                "DeviceName": "xx",
                "Tags": [
                    {
                        "Tag": "xx",
                        "Type": 1,
                        "Name": "xx",
                        "Value": "xx"
                    },
                    {
                        "Tag": "xx",
                        "Type": 1,
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "LogLevel": 1,
                "FirstOnlineTime": 1,
                "DeviceCert": "xx",
                "Imei": "xx",
                "ClientIP": "xx",
                "DevicePsk": "xx",
                "Isp": 1,
                "NbiotDeviceID": "xx",
                "LoraDevEui": "xx",
                "DeviceType": 1,
                "LoginTime": 1,
                "ConnIP": 1,
                "LastUpdateTime": 1,
                "Labels": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "CreateTime": 1,
                "LoraMoteType": 1
            }
        ]
    }
}
```

