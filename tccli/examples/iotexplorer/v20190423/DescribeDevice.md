**Example 1: 查看设备详情**

用于查看设备信息

Input: 

```
tccli iotexplorer DescribeDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName dev01
```

Output: 
```
{
    "Response": {
        "Device": {
            "DeviceName": "deviceName",
            "Status": 0,
            "DevicePsk": "EbhU****==",
            "CreateTime": 1663741732,
            "FirstOnlineTime": 1664354011,
            "LoginTime": 1664356768,
            "LogLevel": 0,
            "Version": "x",
            "DeviceCert": "",
            "DevEUI": "",
            "AppKey": "",
            "DevAddr": "",
            "AppSKey": "",
            "NwkSKey": "",
            "CreatorNickName": "xxx",
            "CreateUserId": 1,
            "EnableState": 0,
            "ProductId": "productId",
            "DeviceType": "设备",
            "ProductName": "name",
            "IsLora": false
        },
        "RequestId": "beee318d-ae0a-44f0-a743-a1744f30c651"
    }
}
```

