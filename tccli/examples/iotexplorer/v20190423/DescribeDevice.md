**Example 1: 查看设备详情**

用于查看设备信息

Input: 

```
tccli iotexplorer DescribeDevice --cli-unfold-argument  \
    --ProductId J2CRPPZ8J4 \
    --DeviceName dev01
```

Output: 
```
{
    "Response": {
        "Device": {
            "DeviceName": "dev",
            "Status": 0,
            "DevicePsk": "EbhU****==",
            "CreateTime": 1663741732,
            "FirstOnlineTime": 1664354011,
            "LoginTime": 1664356768,
            "LogLevel": 0,
            "Version": "v1.0",
            "DeviceCert": "",
            "DevEUI": "",
            "AppKey": "",
            "DevAddr": "",
            "AppSKey": "",
            "NwkSKey": "",
            "CreatorNickName": "d1",
            "CreateUserId": 1,
            "EnableState": 0,
            "ProductId": "J2CRPPZ8J4",
            "DeviceType": "设备",
            "ProductName": "leo",
            "IsLora": false
        },
        "RequestId": "beee318d-ae0a-44f0-a743-a1744f30c651"
    }
}
```

