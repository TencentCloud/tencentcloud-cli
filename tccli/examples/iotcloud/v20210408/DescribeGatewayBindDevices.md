**Example 1: 获取网关绑定的子设备列表**



Input: 

```
tccli iotcloud DescribeGatewayBindDevices --cli-unfold-argument  \
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
        "TotalCount": 1,
        "Devices": [
            {
                "ProductId": "ABCDE12345",
                "DeviceName": "test",
                "BindTime": 1,
                "Tags": []
            }
        ],
        "ProductName": "test",
        "RequestId": "69f65618-600b-4ac4-b8e3-4528a6819078"
    }
}
```

