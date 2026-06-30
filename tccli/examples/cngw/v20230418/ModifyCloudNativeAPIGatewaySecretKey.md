**Example 1: 修改密钥**

修改密钥

Input: 

```
tccli cngw ModifyCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --Name 密钥11 \
    --SecretKeyId secret-xxx \
    --Description 秘钥描述
```

Output: 
```
{
    "Response": {
        "RequestId": "09b30d12-03bf-4631-aa09-4d5a1a4c18e0"
    }
}
```

