**Example 1: 模型API给消费者分组授权**

模型API给消费者分组授权

Input: 

```
tccli cngw AddCloudNativeAPIGatewayConsumerGroupAuth --cli-unfold-argument  \
    --GatewayId gateway-1b59c523 \
    --ResourceType ModelAPI \
    --ResourceId e3aa4fe271c24bb4aa7cca41db5a4e75 \
    --ConsumerGroupIds cg-d4fbcc88676d50
```

Output: 
```
{
    "Response": {
        "RequestId": "45b34a9a-57f7-4c8d-8fb2-150256f637f1"
    }
}
```

