**Example 1: 获取弹性容器集群的接入认证信息**



Input: 

```
tccli tke DescribeEKSClusterCredential --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "Credential": {
            "CACert": "xx",
            "Token": "xx"
        },
        "Addresses": [
            {
                "Ip": "xx",
                "Type": "xx",
                "Port": 1
            },
            {
                "Ip": "xx",
                "Type": "xx",
                "Port": 1
            }
        ],
        "ProxyLB": true,
        "RequestId": "xx",
        "PublicLB": {
            "SecurityPolicies": [
                "xx"
            ],
            "Enabled": true,
            "SecurityGroup": "xx",
            "AllowFromCidrs": [
                "xx"
            ],
            "ExtraParam": "xx"
        },
        "InternalLB": {
            "SubnetId": "xx",
            "Enabled": true
        },
        "Kubeconfig": "apiVersion: v1 \n clusters: \n - cluster: \n     insecure-skip-tls-verify: true\n     server: https://9.3.224.18:10909 \n   name: cls-xxxxxxxx \n contexts: \n - context:\n     cluster: cls-xxxxxxxx \n     user: admin\n  name: master\n current-context: master \n kind: Config \n preferences: {} \n users: \n- \n ame: admin \n  user:\n    token: xxxxlWn8DaQQneFkPWht1Suorkxxxxxx\n"
    }
}
```

