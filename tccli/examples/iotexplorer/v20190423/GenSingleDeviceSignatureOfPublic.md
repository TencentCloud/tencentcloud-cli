**Example 1: 生成单个设备绑定的签名**

生成单个设备绑定的签名,  一般用于APP绑定设备

Input: 

```
tccli iotexplorer GenSingleDeviceSignatureOfPublic --cli-unfold-argument  \
    --DeviceName dev001 \
    --Expire 86400 \
    --ProductId H4EAI7TIZR
```

Output: 
```
{
    "Response": {
        "DeviceSignature": {
            "DeviceName": "dev001",
            "DeviceSignature": "fbaba57679644f29adee486528644a5a"
        },
        "RequestId": "8bbbaa15-9918-4fd9-a70c-dbb47deac0ca"
    }
}
```

