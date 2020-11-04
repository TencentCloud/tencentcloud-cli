**Example 1: 获取设备列表**

根据某个产品ID获取对应的设备列表

Input: 

```
tccli iotexplorer GetDeviceList --cli-unfold-argument  \
    --ProductId ABCDE12345\
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Devices": [
            {
                "DeviceName": "wifi_test",
                "Status": 0,
                "DevicePsk": "",
                "FirstOnlineTime": 1557397755,
                "LoginTime": 1559744044
            },
            {
                "DeviceName": "dev_hu",
                "Status": 0,
                "DevicePsk": "",
                "FirstOnlineTime": 1557235894,
                "LoginTime": 1560328893
            },
            {
                "DeviceName": "dev01",
                "Status": 0,
                "DevicePsk": "",
                "FirstOnlineTime": 1557229181,
                "LoginTime": 1557470791
            }
        ],
        "RequestId": "4ccc27e9-4525-4396-9db3-369b2cd3d28a",
        "Total": 3
    }
}
```

