**Example 1: 批量绑定子设备**



Input: 

```
tccli iotcloud BindDevices --cli-unfold-argument  \
    --GatewayProductId EQPOKD5111 \
    --GatewayDeviceName devGat-001 \
    --ProductId DGRESAG222 \
    --DeviceNames dev01 dev02
```

Output: 
```
{
    "Response": {
        "RequestId": "69f65618-600b-4ac4-b8e3-4528a6819078"
    }
}
```

