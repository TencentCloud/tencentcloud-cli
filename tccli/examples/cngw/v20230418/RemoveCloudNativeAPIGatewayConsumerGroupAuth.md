**Example 1: 从模型API里解除分组授权**



Input: 

```
tccli cngw RemoveCloudNativeAPIGatewayConsumerGroupAuth --cli-unfold-argument  \
    --GatewayId gateway-1b59c523 \
    --ResourceType ModelAPI \
    --ResourceId e3aa4fe271c24bb4aa7cca41db5a4e75 \
    --ConsumerGroupIds cg-d4fbcc88676d50
```

Output: 
```
{
    "Response": {
        "RequestId": "2eb7e299-cd5c-4aaf-bbb2-b02ca61a5d49"
    }
}
```

