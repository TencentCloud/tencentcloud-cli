**Example 1: 获取设备列表**

根据某个产品ID获取对应的设备列表

Input: 

```
tccli iotexplorer GetDeviceList --cli-unfold-argument  \
    --ProductId NS74VEP2HY \
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
                "DevicePsk": "tgrgsg=",
                "CreateTime": 0,
                "FirstOnlineTime": 0,
                "LoginTime": 0,
                "LogLevel": 0,
                "Version": "v1",
                "DeviceCert": "",
                "DevEUI": "",
                "AppKey": "",
                "DevAddr": "",
                "AppSKey": "",
                "NwkSKey": "",
                "CreatorNickName": "leo",
                "CreateUserId": 635261,
                "EnableState": 0,
                "ProductId": "NS74VEP2HY",
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

