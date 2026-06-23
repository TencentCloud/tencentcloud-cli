**Example 1: 修改消费者信息**

修改消费者信息

Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayConsumer --cli-unfold-argument  \
    --GatewayId gateway-e0e9a565 \
    --ConsumerId c31f5dd7-eab5-4e77-ac18-31add3c94a9d \
    --Name 消费者1 \
    --Description 消费者描述
```

Output: 
```
{
    "Response": {
        "RequestId": "2d793cfa-f682-47f8-b92d-0cb656c75c42"
    }
}
```

