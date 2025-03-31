**Example 1: 获取网关绑定的子设备列表**



Input: 

```
tccli iotexplorer DescribeGatewayBindDevices --cli-unfold-argument  \
    --GatewayProductId ' J2CRPPZ8J4' \
    --GatewayDeviceName d1 \
    --Offset 0 \
    --Limit 10 \
    --ProductId ' RFVRPPZ5G'
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Devices": [
            {
                "ProductId": "J2CRPPZ8J4",
                "DeviceName": "d1"
            }
        ],
        "ProductName": "产品名称",
        "RequestId": "69f65618-600b-4ac4-b8e3-454r819078"
    }
}
```

