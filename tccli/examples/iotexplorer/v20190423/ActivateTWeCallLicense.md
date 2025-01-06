**Example 1: 成功激活示例**



Input: 

```
tccli iotexplorer ActivateTWeCallLicense --cli-unfold-argument  \
    --PkgType 1 \
    --DeviceList.0.Sn productId_deviceName
```

Output: 
```
{
    "Response": {
        "RequestId": "3edc-45tg",
        "FailureList": [],
        "SuccessList": [
            {
                "ModelId": "modelId",
                "Sn": "productId_deviceName",
                "ExpireTime": 356123
            }
        ]
    }
}
```

