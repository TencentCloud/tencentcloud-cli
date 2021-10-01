**Example 1: 查看集群认证配置**



Input: 

```
tccli tke DescribeClusterAuthenticationOptions --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "ServiceAccounts": {
            "JWKSURI": "https://cls-xxxxxxxx.ccs.tencent-cloud.com/openid/v1/jwks",
            "Issuer": "https://cls-xxxxxxxx.ccs.tencent-cloud.com"
        },
        "LatestOperationState": "Updating"
    }
}
```

