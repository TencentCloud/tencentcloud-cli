**Example 1: 获取 NFC 的小程序 scheme**

该接口用于获取用于 NFC 的小程序 scheme 码，适用于 NFC 拉起小程序的业务场景。

Input: 

```
tccli iotexplorer GenerateNFCScheme --cli-unfold-argument  \
    --DeviceId product-xxx/device-xxx \
    --Path /pages/publishHomework/publishHomework
```

Output: 
```
{
    "Response": {
        "OpenLink": "Scheme Payload",
        "RequestId": "ebb39788-8b97-4a85-8e34-192c09e29376"
    }
}
```

