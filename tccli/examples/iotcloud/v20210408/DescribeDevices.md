**Example 1: 获取设备列表**



Input: 

```
tccli iotcloud DescribeDevices --cli-unfold-argument  \
    --ProductId UTY6QRLMQY \
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
                "CertState": 0,
                "ClientIP": "",
                "ConnIP": 0,
                "CreateTime": 1741680312,
                "CreateUserId": 630811165,
                "DeviceCert": "",
                "DeviceName": "dev03",
                "DevicePsk": "",
                "DeviceType": 0,
                "EnableState": 1,
                "FirmwareUpdateTime": 0,
                "FirstOnlineTime": 0,
                "Imei": "",
                "Isp": 0,
                "Labels": [],
                "LastOfflineTime": 0,
                "LastUpdateTime": 1741680312,
                "LogLevel": 0,
                "LoginTime": 0,
                "LoraDevEui": "",
                "LoraMoteType": 0,
                "NBIoTDeviceID": "",
                "Online": 3,
                "Tags": [
                    {
                        "Name": "",
                        "Tag": "category",
                        "Type": 2,
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Tag": "note",
                        "Type": 2,
                        "Value": ""
                    }
                ],
                "Version": ""
            },
            {
                "CertState": 0,
                "ClientIP": "",
                "ConnIP": 0,
                "CreateTime": 1740626513,
                "CreateUserId": 630833365,
                "DeviceCert": "",
                "DeviceName": "dev000001",
                "DevicePsk": "",
                "DeviceType": 0,
                "EnableState": 1,
                "FirmwareUpdateTime": 0,
                "FirstOnlineTime": 0,
                "Imei": "",
                "Isp": 0,
                "Labels": [],
                "LastOfflineTime": 0,
                "LastUpdateTime": 1740626513,
                "LogLevel": 0,
                "LoginTime": 0,
                "LoraDevEui": "",
                "LoraMoteType": 0,
                "NBIoTDeviceID": "",
                "Online": 3,
                "Tags": [
                    {
                        "Name": "",
                        "Tag": "category",
                        "Type": 2,
                        "Value": ""
                    },
                    {
                        "Name": "",
                        "Tag": "note",
                        "Type": 2,
                        "Value": ""
                    }
                ],
                "Version": ""
            }
        ],
        "RequestId": "8dcf4055-ba4b-4ae3-aced-d841c8202faa",
        "TotalCount": 2
    }
}
```

