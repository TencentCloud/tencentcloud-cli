**Example 1: 创建消费者**



Input: 

```
tccli tse CreateCloudNativeAPIGatewayConsumer --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --Name 消费者 \
    --Description 消费者描述
```

Output: 
```
{
    "Response": {
        "RequestId": "3575b458-81a9-49ea-8a49-64432fe22ed0",
        "Result": {
            "ID": "consumer-6021c8b0",
            "Success": true
        }
    }
}
```

