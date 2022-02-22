**Example 1: 查询绑定到家庭的网关设备的子设备列表**



Input: 

```
tccli iotexplorer DescribeGatewaySubDeviceList --cli-unfold-argument  \
    --GatewayProductId productId \
    --GatewayDeviceName deviceName \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "DeviceList": [
            {
                "ProductId": "ZOPEBSS",
                "DeviceName": "sub001",
                "DeviceId": "ZOPEBSS/sub001",
                "AliasName": "aaaaa",
                "FamilyId": "f_9b309d",
                "RoomId": "0",
                "IconUrl": "",
                "IconUrlGrid": "",
                "CreateTime": 1627472149,
                "UpdateTime": 1627472149
            }
        ],
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e",
        "Total": 1
    }
}
```

