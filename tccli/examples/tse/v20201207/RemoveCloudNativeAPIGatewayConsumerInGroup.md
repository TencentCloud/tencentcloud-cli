**Example 1: 从消费者组里移除消费者**



Input: 

```
tccli tse RemoveCloudNativeAPIGatewayConsumerInGroup --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --ConsumerGroupId cg-6021c8b0 \
    --ConsumerIds consumer-d6cdf6af
```

Output: 
```
{
    "Response": {
        "RequestId": "14e46e9e-fa3d-4bdc-86bc-b73a8a69239c"
    }
}
```

