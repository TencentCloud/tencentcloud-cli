**Example 1: 集群的密钥信息**

集群的密钥信息

Input: 

```
tccli tke DescribeClusterSecurity --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "UserName": "admin",
        "Domain": "cls-7ph3twqe.ccs.tencent-cloud.com",
        "CertificationAuthority": "",
        "Kubeconfig": "",
        "PgwEndpoint": "0.0.0.0",
        "JnsGwEndpoint": "127.0.0.1:8080",
        "RequestId": "5f792091-66a7-40fc-8043-4d8b9537fa44",
        "SecurityPolicy": [
            "192.168.0.1"
        ],
        "ClusterExternalEndpoint": "https://127.0.0.1",
        "Password": ""
    }
}
```

