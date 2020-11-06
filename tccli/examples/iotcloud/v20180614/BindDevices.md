**Example 1: 批量绑定子设备**



Input: 

```
tccli iotcloud BindDevices --cli-unfold-argument  \
    --GatewayProductId 12345ABCDE \
    --GatewayDeviceName test \
    --ProductId ABCDE12345 \
    --DeviceNames test0 test1
```

Output: 
```
{
    "Response": {
        "RequestId": "69f65618-600b-4ac4-b8e3-4528a6819078"
    }
}
```

