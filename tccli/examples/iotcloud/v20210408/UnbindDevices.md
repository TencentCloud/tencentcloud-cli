**Example 1: 批量解绑子设备（旧）**



Input: 

```
tccli iotcloud UnbindDevices --cli-unfold-argument  \
    --GatewayProductId EQPOKD5111 \
    --GatewayDeviceName gateway-001 \
    --ProductId EQPOKD5222 \
    --DeviceNames dev-001 dev-002
```

Output: 
```
{
    "Response": {
        "RequestId": "69f65618-600b-4ac4-b8e3-4528a6819078"
    }
}
```

