**Example 1: 修改消费者分组**



Input: 

```
tccli tse ModifyCloudNativeAPIGatewayConsumerGroup --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --ConsumerGroupId cg-6021c8b0 \
    --Name 消费者组 \
    --Description 消费者分组描述 \
    --Status Disable
```

Output: 
```
{
    "Response": {
        "RequestId": "905b39a5-5165-4d80-a338-1a1b63f28f34"
    }
}
```

