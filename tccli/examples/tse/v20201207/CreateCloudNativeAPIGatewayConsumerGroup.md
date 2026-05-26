**Example 1: 创建消费者分组默认开启**

创建消费者分组，默认开启

Input: 

```
tccli tse CreateCloudNativeAPIGatewayConsumerGroup --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --Name 消费者组 \
    --Description 消费者组1 \
    --Status Enable
```

Output: 
```
{
    "Response": {
        "RequestId": "3575b458-81a9-49ea-8a49-64432fe22ed0",
        "Result": {
            "ID": "cg-6021c8b0",
            "Success": true
        }
    }
}
```

