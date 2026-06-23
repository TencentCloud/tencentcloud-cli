**Example 1: 创建消费者分组**



Input: 

```
tccli cngw CreateCloudNativeAPIGatewayConsumerGroup --cli-unfold-argument  \
    --GatewayId gateway-73a0405d \
    --Name testgroup \
    --Status Enable \
    --Description 创建消费者分组
```

Output: 
```
{
    "Response": {
        "Result": {
            "ID": "cg-3bb9e0c9cb9df4",
            "Success": true
        },
        "RequestId": "48345f8b-601f-492c-8643-25566660dd01"
    }
}
```

