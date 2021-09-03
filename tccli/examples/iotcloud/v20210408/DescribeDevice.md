**Example 1: 查看设备详情示例**



Input: 

```
tccli iotcloud DescribeDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName abc
```

Output: 
```
{
    "Response": {
        "EnableState": 1,
        "LastOfflineTime": 1,
        "Version": "xx",
        "CertState": 1,
        "Online": 1,
        "FirmwareUpdateTime": 1,
        "DeviceName": "xx",
        "Tags": [
            {
                "Tag": "Key",
                "Type": 1,
                "Name": "Key",
                "Value": "Key"
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
        "Imei": "Imei",
        "ClientIP": "127.0.0.1",
        "DevicePsk": "DevicePsk",
        "Isp": 1,
        "NbiotDeviceID": "123124",
        "LoraDevEui": "xx",
        "DeviceType": 1,
        "RequestId": "xx",
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
        "LoraMoteType": 1,
        "CreateUserId": 0
    }
}
```

