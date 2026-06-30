**Example 1: 解绑密钥**



Input: 

```
tccli cngw UnbindCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --ResourceType Consumer \
    --ResourceIds c31f5dd7-eab5-4e77-ac18-31add3c94a9d \
    --SecretKeyId secret-3bc27fec
```

Output: 
```
{
    "Response": {
        "RequestId": "fe5e247d-cab5-4ddc-a02c-4b50e0966fed"
    }
}
```

