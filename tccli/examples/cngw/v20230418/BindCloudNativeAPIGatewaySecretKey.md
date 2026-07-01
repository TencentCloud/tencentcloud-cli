**Example 1: 添加消费者凭证**

消费者凭证， ResourceIds 只能传一个

Input: 

```
tccli cngw BindCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --ResourceType Consumer \
    --ResourceIds c31f5dd7-eab5-4e77-ac18-31add3c94a9d \
    --SecretKeyId secret-3bc27fec
```

Output: 
```
{
    "Response": {
        "RequestId": "2c3f37e8-5bc2-416b-b2e1-14c3775fd24c",
        "Result": true
    }
}
```

