**Example 1: 取消子设备产品与网关设备产品的关联**

取消子设备产品与网关设备产品的关联

Input: 

```
tccli iot UnassociateSubDeviceFromGatewayProduct --cli-unfold-argument  \
    --SubDeviceProductId iot-4e0wsxpi \
    --GatewayProductId iot-43e0wsxas
```

Output: 
```
{
    "Response": {
        "RequestId": "b78d722c-c32c-4108-b9d8-a75be705e227"
    }
}
```

