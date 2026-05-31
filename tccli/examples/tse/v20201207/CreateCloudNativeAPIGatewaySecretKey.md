**Example 1: 创建KMS秘钥**



Input: 

```
tccli tse CreateCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --SecretType ApiKey \
    --Name 测试KMS密钥 \
    --GenerateType KMS \
    --ResourceType Consumer \
    --KmsKeyName XX \
    --KmsKeyVersion v1 \
    --Description 测试密钥
```

Output: 
```
{
    "Response": {
        "RequestId": "3f6008b8-249c-4b5c-a5ea-09bedb2a5b3b",
        "Result": {
            "ID": "secret-30859974",
            "Success": true
        }
    }
}
```

**Example 2: 创建自动生成密钥**



Input: 

```
tccli tse CreateCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --SecretType ApiKey \
    --Name 测试系统密钥 \
    --GenerateType System \
    --ResourceType Consumer \
    --Description 密钥
```

Output: 
```
{
    "Response": {
        "RequestId": "f0edc69d-f575-44da-ba7a-b40656fcf878",
        "Result": {
            "ID": "secret-152eb264",
            "Success": true
        }
    }
}
```

**Example 3: 创建自定义密钥**



Input: 

```
tccli tse CreateCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --SecretType ApiKey \
    --Name 测试自定义密钥 \
    --GenerateType Custom \
    --ResourceType Consumer \
    --SecretValue sk-xxxxxxxx \
    --Description 测试密钥
```

Output: 
```
{
    "Response": {
        "RequestId": "173ebf7b-7beb-442d-bc4f-7a66eebd8264",
        "Result": {
            "ID": "secret-c3966447",
            "Success": true
        }
    }
}
```

