**Example 1: 获取边缘计算集群的接入认证信息**



Input: 

```
tccli tke DescribeTKEEdgeClusterCredential --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
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
        "GridDaemon": "yes",
        "PublicLB": {
            "Enabled": true,
            "AllowFromCidrs": [
                "xx"
            ]
        },
        "InternalLB": {
            "SubnetId": [
                "xx"
            ],
            "Enabled": true
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

