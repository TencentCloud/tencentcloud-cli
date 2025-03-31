**Example 1: 批量绑定子设备**



Input: 

```
tccli iotexplorer BindDevices --cli-unfold-argument  \
    --GatewayProductId J2CRPPZ8J4 \
    --GatewayDeviceName d1 \
    --ProductId RF5t6H2T \
    --DeviceNames dec
```

Output: 
```
{
    "Response": {
        "RequestId": "fee15c53-91ac-488d-855d-c02d9f5f3d91"
    }
}
```

