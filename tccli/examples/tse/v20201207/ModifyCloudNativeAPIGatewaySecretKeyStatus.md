**Example 1: 启用密钥**



Input: 

```
tccli tse ModifyCloudNativeAPIGatewaySecretKeyStatus --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --Status Enable \
    --SecretKeyId secret-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b877a25a-207b-47b2-ad4b-1ad1d0345971"
    }
}
```

**Example 2: 禁用密钥**



Input: 

```
tccli tse ModifyCloudNativeAPIGatewaySecretKeyStatus --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --Status Disable \
    --SecretKeyId secret-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b877a25a-207b-47b2-ad4b-1ad1d0345971"
    }
}
```

