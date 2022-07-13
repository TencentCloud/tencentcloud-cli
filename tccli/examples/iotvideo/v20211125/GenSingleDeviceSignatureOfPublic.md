**Example 1: 生成单个设备绑定的签名**

生成单个设备绑定的签名, 一般用于APP绑定设备

Input: 

```
tccli iotvideo GenSingleDeviceSignatureOfPublic --cli-unfold-argument  \
    --DeviceName test_76854689_1 \
    --Expire 86400 \
    --ProductId L78ASO6Z95
```

Output: 
```
{
    "Response": {
        "RequestId": "679e42ce-ee1b-408f-8e1f-5b5766614ec7",
        "DeviceSignature": {
            "DeviceName": "test_76854689_1",
            "DeviceSignature": "751c625f1d674be09ab422883f16xxxx"
        }
    }
}
```

