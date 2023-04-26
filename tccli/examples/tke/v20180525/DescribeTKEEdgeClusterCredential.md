**Example 1: 获取边缘计算集群的接入认证信息**

获取边缘集群的认证信息，其中包含kubeconfig文件

Input: 

```
tccli tke DescribeTKEEdgeClusterCredential --cli-unfold-argument  \
    --ClusterId cls-1234abcd
```

Output: 
```
{
    "Response": {
        "Addresses": [
            {
                "Type": "advertise",
                "Ip": "169.254.128.200",
                "Port": 60002
            },
            {
                "Type": "public",
                "Ip": "100.98.109.15",
                "Port": 11126
            }
        ],
        "Credential": {
            "CACert": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FULQo=",
            "Token": "WBnCe69iqui0HuEZJ0Yac2hvwxQ1jG0j"
        },
        "CoreDns": "yes",
        "HealthRegion": "yes",
        "Health": "yes",
        "UnitCluster": "yes",
        "GridDaemon": "yes",
        "PublicLB": {
            "Enabled": true,
            "AllowFromCidrs": [
                "160/254.0.0/16"
            ]
        },
        "InternalLB": {
            "SubnetId": [
                "vpc-12345"
            ],
            "Enabled": true
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

