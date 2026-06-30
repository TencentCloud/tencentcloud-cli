**Example 1: 添加消费者到分组**



Input: 

```
tccli cngw AddCloudNativeAPIGatewayConsumerInGroup --cli-unfold-argument  \
    --GatewayId gateway-4e588095 \
    --ConsumerGroupId cg-9a130aba0f747c \
    --ConsumerIds c31f5dd7-eab5-4e77-ac18-31add3c94a9d
```

Output: 
```
{
    "Response": {
        "RequestId": "828b6c28-24d2-4988-97d7-e12e4fa8acef",
        "Result": true
    }
}
```

