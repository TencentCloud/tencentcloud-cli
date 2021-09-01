**Example 1: 用户绑定设备**

应用与智能家居场景，绑定设备前需获取绑定设备的签名

Input: 

```
tccli iot AppSecureAddDevice --cli-unfold-argument  \
    --AccessToken xxx \
    --DeviceSignature xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3d846510-444b-4b6d-a8af-6d2b5a21981b",
        "AppDevice": {
            "Region": "ap-guangzhou",
            "ProductId": "iot-4e0wsxpi",
            "DeviceName": "aaaa",
            "CreateTime": "2018-07-06 11:49:32",
            "UpdateTime": "2018-07-06 11:49:32",
            "DeviceId": "ap-guangzhou/iot-4e0wsxpi/aaaa",
            "AliasName": ""
        }
    }
}
```

