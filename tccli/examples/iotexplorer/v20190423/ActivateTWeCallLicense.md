**Example 1: 成功激活示例**



Input: 

```
tccli iotexplorer ActivateTWeCallLicense --cli-unfold-argument  \
    --PkgType 1 \
    --MiniProgramAppId abc \
    --DeviceList.0.ModelId 1qaz \
    --DeviceList.0.Sn p/d
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
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

