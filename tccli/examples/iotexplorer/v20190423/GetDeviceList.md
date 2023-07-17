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
                "DeviceName": "test",
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
                "EnableState": 0,
                "ProductId": "PR***TA",
                "DeviceType": "设备",
                "ProductName": "产品名称",
                "IsLora": false
            }
        ],
        "RequestId": "219a59ba-fdd0-4214-8db-71da9fe28",
        "Total": 1
    }
}
```

