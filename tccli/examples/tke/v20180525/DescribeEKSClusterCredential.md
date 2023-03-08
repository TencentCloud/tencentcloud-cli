**Example 1: 获取弹性容器集群的接入认证信息**



Input: 

```
tccli tke DescribeEKSClusterCredential --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "Credential": {
            "CACert": "",
            "Token": ""
        },
        "Addresses": [
            {
                "Ip": "127.0.0.1",
                "Type": "Public",
                "Port": 443
            }
        ],
        "ProxyLB": true,
        "RequestId": "0d1f4439-266b-4ea1-8c97-b0cca5eed7io",
        "PublicLB": {
            "SecurityPolicies": [
                "192.168.1.1"
            ],
            "Enabled": true,
            "SecurityGroup": "",
            "AllowFromCidrs": [
                ""
            ],
            "ExtraParam": ""
        },
        "InternalLB": {
            "SubnetId": "",
            "Enabled": true
        },
        "Kubeconfig": "apiVersion: v1 \n clusters: \n - cluster: \n     insecure-skip-tls-verify: true\n     server: https://9.3.224.18:10909 \n   name: cls-7ph3twqe \n contexts: \n - context:\n     cluster: cls-7ph3twqe \n     user: admin\n  name: master\n current-context: master \n kind: Config \n preferences: {} \n users: \n- \n ame: admin \n  user:\n    token: wqwwqlWn8DaQQneFkPWht1Suorktrwewq\n"
    }
}
```

