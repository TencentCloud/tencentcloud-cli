**Example 1: 修改集群认证配置**



Input: 

```
tccli tke ModifyClusterAuthenticationOptions --cli-unfold-argument  \
    --ServiceAccounts.JWKSURI https://cls-xxxxxxxx.ccs.tencent-cloud.com/openid/v1/jwks \
    --ServiceAccounts.Issuer https://cls-xxxxxxxx.ccs.tencent-cloud.com \
    --ServiceAccounts.AutoCreateDiscoveryAnonymousAuth True \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

