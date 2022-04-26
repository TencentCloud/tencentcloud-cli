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
            "Status": 0,
            "DeviceName": "xx",
            "NwkSKey": "xx",
            "Version": "xx",
            "DevicePsk": "xx",
            "DevAddr": "xx",
            "LogLevel": 0,
            "CreatorNickName": "xx",
            "AppSKey": "xx",
            "EnableState": 0,
            "LoginTime": 0,
            "ProductName": "xx",
            "CreateUserId": 0,
            "FirstOnlineTime": 0,
            "DeviceType": "xx",
            "DeviceCert": "xx",
            "DevEUI": "xx",
            "CreateTime": 0,
            "AppKey": "xx",
            "ProductId": "xx"
        },
        "RequestId": "xx"
    }
}
```

