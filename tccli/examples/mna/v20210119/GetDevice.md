**Example 1: 获取指定id设备信息**



Input: 

```
tccli mna GetDevice --cli-unfold-argument  \
    --DeviceId mna-xxx
```

Output: 
```
{
    "Response": {
        "DeviceDetails": {
            "DeviceBaseInfo": {
                "DeviceName": "dev",
                "Remark": "xx",
                "DeviceId": "mna-xxx",
                "LastTime": "1",
                "CreateTime": "1"
            },
            "DeviceNetInfo": [
                {
                    "SignalStrength": -85,
                    "Vendor": 1,
                    "DataTx": 10,
                    "UploadLimit": 100,
                    "DownloadLimit": 100,
                    "Rat": 2,
                    "PublicIp": "xxx.xxx.xxx.xx",
                    "State": 0,
                    "DataRx": 10,
                    "DataEnable": true,
                    "Type": 0,
                    "NetInfoName": "xx"
                },
                {
                    "SignalStrength": -90,
                    "Vendor": 1,
                    "DataTx": 10,
                    "UploadLimit": 100,
                    "DownloadLimit": 100,
                    "Rat": 2,
                    "PublicIp": "xxx.xxx.xxx.xx",
                    "State": 0,
                    "DataRx": 10,
                    "DataEnable": true,
                    "Type": 1,
                    "NetInfoName": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

