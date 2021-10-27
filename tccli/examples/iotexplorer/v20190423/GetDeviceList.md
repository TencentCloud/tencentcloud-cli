**Example 1: 获取设备列表**

根据某个产品ID获取对应的设备列表

Input: 

```
tccli iotexplorer GetDeviceList --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --ProjectId 12 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Devices": [
            {
                "DeviceName": "d1",
                "Status": 0,
                "DevicePsk": "",
                "CreateTime": 0,
                "FirstOnlineTime": 0,
                "LoginTime": 0,
                "LogLevel": 0,
                "Version": "",
                "DeviceCert": "",
                "DevEUI": "",
                "AppKey": "",
                "DevAddr": "",
                "AppSKey": "",
                "NwkSKey": "",
                "CreatorNickName": "",
                "CreateUserId": 0,
                "EnableState": 1,
                "ProductId": "8OZC697IJ9",
                "DeviceType": "网关",
                "ProductName": "1aoioii9_test"
            },
            {
                "DeviceName": "d1",
                "Status": 0,
                "DevicePsk": "",
                "CreateTime": 0,
                "FirstOnlineTime": 0,
                "LoginTime": 0,
                "LogLevel": 0,
                "Version": "",
                "DeviceCert": "",
                "DevEUI": "",
                "AppKey": "",
                "DevAddr": "",
                "AppSKey": "",
                "NwkSKey": "",
                "CreatorNickName": "",
                "CreateUserId": 0,
                "EnableState": 1,
                "ProductId": "H4EAI7TIZR",
                "DeviceType": "设备",
                "ProductName": "1aoioii9_智能灯"
            },
            {
                "DeviceName": "d10",
                "Status": 0,
                "DevicePsk": "",
                "CreateTime": 0,
                "FirstOnlineTime": 0,
                "LoginTime": 0,
                "LogLevel": 0,
                "Version": "",
                "DeviceCert": "",
                "DevEUI": "",
                "AppKey": "",
                "DevAddr": "",
                "AppSKey": "",
                "NwkSKey": "",
                "CreatorNickName": "",
                "CreateUserId": 0,
                "EnableState": 1,
                "ProductId": "H4EAI7TIZR",
                "DeviceType": "设备",
                "ProductName": "1aoioii9_智能灯"
            }
        ],
        "RequestId": "8bbbaa15-9918-4fd9-a70c-dbb47dwac0ca",
        "Total": 15
    }
}
```

