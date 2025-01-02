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
        "LatestOperationState": "",
        "OIDCConfig": {
            "AutoCreateClientId": null,
            "AutoCreateOIDCConfig": null,
            "AutoInstallPodIdentityWebhookAddon": null
        },
        "RequestId": "844ea54c-4271-48a7-b6da-686f44782d91",
        "ServiceAccounts": {
            "AutoCreateDiscoveryAnonymousAuth": null,
            "Issuer": "https://kubernetes.default.svc.cluster.local",
            "JWKSURI": null,
            "UseTKEDefault": null
        }
    }
}
```

