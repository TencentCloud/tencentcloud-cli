**Example 1: 批量解绑子设备**



Input: 

```
tccli iotexplorer UnbindDevices --cli-unfold-argument  \
    --GatewayProductId ' J2CRPPZ8J4' \
    --GatewayDeviceName d1 \
    --ProductId ' RFVZ8J4' \
    --DeviceNames dev0
```

Output: 
```
{
    "Response": {
        "RequestId": "fee15c53-91ac-488d-855d-c02d9f5f3d91"
    }
}
```

