**Example 1: 集群的密钥信息**

集群的密钥信息

Input: 

```
tccli tke DescribeClusterSecurity --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "UserName": "xx",
        "Domain": "xx",
        "CertificationAuthority": "xx",
        "Kubeconfig": "xx",
        "PgwEndpoint": "xx",
        "JnsGwEndpoint": "xx",
        "RequestId": "xx",
        "SecurityPolicy": [
            "xx"
        ],
        "ClusterExternalEndpoint": "xx",
        "Password": "xx"
    }
}
```

