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
        }
    }
}
```

