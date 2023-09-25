**Example 1: 创建云原生网关证书**

创建云原生网关证书

Input: 

```
tccli tse CreateCloudNativeAPIGatewayCertificate --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --Name a \
    --BindDomains bbc.com \
    --CertId 12412rew43-5fdsf35
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

