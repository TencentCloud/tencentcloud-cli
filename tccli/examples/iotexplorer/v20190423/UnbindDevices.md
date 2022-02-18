**Example 1: 批量解绑子设备**



Input: 

```
tccli iotexplorer UnbindDevices --cli-unfold-argument  \
    --GatewayProductId 12345ABCDE \
    --GatewayDeviceName test \
    --ProductId ABCDE12345 \
    --DeviceNames test0
```

Output: 
```
{
    "Response": {
        "RequestId": "fee15c53-91ac-488d-855d-c02d9f5f3d91"
    }
}
```

