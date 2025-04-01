**Example 1: 查询设备绑定的网关设备**



Input: 

```
tccli iotexplorer DescribeDeviceBindGateway --cli-unfold-argument  \
    --ProductId LAEG4YJE \
    --DeviceName subdev
```

Output: 
```
{
    "Response": {
        "GatewayDeviceName": "gwdev",
        "GatewayProductId": "NJ27OVLZ",
        "GatewayName": "网关名",
        "GatewayProductOwnerName": "NJ27OVLZ",
        "GatewayProductOwnerUin": "1852369542",
        "RequestId": "ef9ec631-7337-481b-a6c3-59a34b500198"
    }
}
```

