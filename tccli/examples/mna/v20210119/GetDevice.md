**Example 1: 获取指定id设备信息**

获取设备基本信息和网络信息

Input: 

```
tccli mna GetDevice --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DeviceDetails": {
            "BusinessDownRate": 0,
            "BusinessUpRate": 443292176.8,
            "DeviceBaseInfo": {
                "CreateTime": "1662722094000",
                "DeviceId": "mna-94p8c5zyst",
                "DeviceName": "yusheng-test2",
                "LastTime": "1675242602000",
                "Remark": "yusheng-test"
            },
            "DeviceNetInfo": [
                {
                    "DataEnable": false,
                    "DataRx": 0,
                    "DataTx": 0,
                    "DownRate": 463128.799998,
                    "DownloadLimit": "0",
                    "NetInfoName": "eth0",
                    "PublicIp": "9.223.110.232",
                    "Rat": 0,
                    "SignalStrength": 0,
                    "State": 0,
                    "Type": 0,
                    "UpRate": 27040465.6,
                    "UploadLimit": "0",
                    "Vendor": 0
                },
                {
                    "DataEnable": false,
                    "DataRx": 0,
                    "DataTx": 0,
                    "DownRate": 4415987.2,
                    "DownloadLimit": "0",
                    "NetInfoName": "eth1",
                    "PublicIp": "9.223.96.218",
                    "Rat": 0,
                    "SignalStrength": 0,
                    "State": 0,
                    "Type": 0,
                    "UpRate": 428871766.399999,
                    "UploadLimit": "0",
                    "Vendor": 0
                }
            ],
            "GatewaySite": "gz"
        },
        "RequestId": "2ca4e2e9-f4a1-4b24-b88a-b7523099c123"
    }
}
```

