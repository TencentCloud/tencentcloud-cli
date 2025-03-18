**Example 1: 获取网关绑定的子设备列表**



Input: 

```
tccli iotcloud DescribeGatewayBindDevices --cli-unfold-argument  \
    --GatewayProductId EQPOKD5111 \
    --GatewayDeviceName devGat-001 \
    --Offset 0 \
    --Limit 10 \
    --ProductId EQPOKD5111
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Devices": [
            {
                "ProductId": "EQPOKD5111",
                "DeviceName": "devGat-001",
                "BindTime": 1,
                "Tags": []
            }
        ],
        "ProductName": "dev-001",
        "RequestId": "69f65618-600b-4ac4-b8e3-4528a6819078"
    }
}
```

