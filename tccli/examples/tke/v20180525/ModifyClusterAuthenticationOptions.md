**Example 1: 修改集群认证配置**

修改集群认证配置

Input: 

```
tccli tke ModifyClusterAuthenticationOptions --cli-unfold-argument  \
    --ServiceAccounts.JWKSURI https://cls-7ph3twqe.ccs.tencent-cloud.com/openid/v1/jwks \
    --ServiceAccounts.Issuer https://cls-7ph3twqe.ccs.tencent-cloud.com \
    --ServiceAccounts.AutoCreateDiscoveryAnonymousAuth True \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

