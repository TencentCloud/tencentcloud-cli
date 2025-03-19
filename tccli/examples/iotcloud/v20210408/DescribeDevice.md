**Example 1: 查看设备详情示例**



Input: 

```
tccli iotcloud DescribeDevice --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --DeviceName dev-001
```

Output: 
```
{
    "Response": {
        "EnableState": 1,
        "LastOfflineTime": 1,
        "Version": "2018-06-14",
        "CertState": 1,
        "Online": 1,
        "FirmwareUpdateTime": 1,
        "DeviceName": "Device001",
        "Tags": [
            {
                "Tag": "Key",
                "Type": 1,
                "Name": "Key",
                "Value": "Key"
            },
            {
                "Tag": "tag-a",
                "Type": 1,
                "Name": "tag-name",
                "Value": "tag-value"
            }
        ],
        "LogLevel": 1,
        "FirstOnlineTime": 1,
        "DeviceCert": "52352",
        "Imei": "Imei",
        "ClientIP": "127.0.0.1",
        "DevicePsk": "4534623",
        "Isp": 1,
        "NBIoTDeviceID": "12122124",
        "LoraDevEui": "your eui",
        "DeviceType": 1,
        "RequestId": "2abji99uojssd88",
        "LoginTime": 1,
        "ConnIP": 1,
        "LastUpdateTime": 1,
        "Labels": [
            {
                "Value": "value-a",
                "Key": "key-a"
            }
        ],
        "CreateTime": 1,
        "LoraMoteType": 1,
        "CreateUserId": 0
    }
}
```

