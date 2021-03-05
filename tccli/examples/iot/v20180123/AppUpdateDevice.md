**Example 1: 应用更新设备信息**

应用更新设备信息

Input: 

```
tccli iot AppUpdateDevice --cli-unfold-argument  \
    --AccessToken xxx \
    --ProductId iot-a8ojgbji \
    --DeviceName aaa \
    --AliasName nick
```

Output: 
```
{
    "Response": {
        "RequestId": "bc2f59a6-9741-4737-ab3e-5c65d9385330",
        "AppDevice": {
            "AliasName": "nick",
            "Region": "ap-guangzhou",
            "ProductId": "iot-a8ojgbji",
            "DeviceName": "aaa"
        }
    }
}
```

