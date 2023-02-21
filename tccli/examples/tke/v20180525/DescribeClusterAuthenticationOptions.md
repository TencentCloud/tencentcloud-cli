**Example 1: 查看集群认证配置**

查看集群认证配置

Input: 

```
tccli tke DescribeClusterAuthenticationOptions --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "RequestId": "24564577-a642-4164-8752-4668d4ca8886",
        "ServiceAccounts": {
            "JWKSURI": "https://cls-7ph3twqe.ccs.tencent-cloud.com/openid/v1/jwks",
            "Issuer": "https://cls-7ph3twqe.ccs.tencent-cloud.com"
        },
        "OIDCConfig": {
            "AutoCreateOIDCConfig": true,
            "AutoInstallPodIdentityWebhookAddon": true,
            "AutoCreateClientId": [
                "84ec9912f0be4066be862afaff9d3c48"
            ]
        },
        "LatestOperationState": "Updating"
    }
}
```

