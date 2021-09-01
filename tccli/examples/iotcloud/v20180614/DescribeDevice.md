**Example 1: 查看设备详情示例**



Input: 

```
tccli iotcloud DescribeDevice --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --DeviceName abc
```

Output: 
```
{
    "Response": {
        "Tags": [
            {
                "Tag": "category",
                "Type": 2,
                "Value": ""
            },
            {
                "Tag": "note",
                "Type": 2,
                "Value": ""
            }
        ],
        "DeviceName": "",
        "DeviceCert": "-----BEGIN CERTIFICATE-----\nIIDS...Fw==\n-----END CERTIFICATE-----\n",
        "Online": 0,
        "ConnIP": 0,
        "LoginTime": 0,
        "Version": "",
        "LastUpdateTime": 0,
        "DevicePsk": "",
        "DeviceType": 3,
        "Imei": "",
        "Isp": 0,
        "NbiotDeviceID": "",
        "LoraDevEui": "",
        "LoraMoteType": 0,
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

