**Example 1: 获取网关绑定的子设备列表**



Input: 

```
tccli iotexplorer DescribeGatewayBindDevices --cli-unfold-argument  \
    --GatewayProductId 12345ABCDE \
    --GatewayDeviceName test \
    --Offset 0 \
    --Limit 10 \
    --ProductId ABCDE12345
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Devices": [
            {
                "ProductId": "ABCDE12345",
                "DeviceName": "test"
            }
        ],
        "ProductName": "test",
        "RequestId": "69f65618-600b-4ac4-b8e3-4528a6819078"
    }
}
```

