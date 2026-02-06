**Example 1: 查询多通道安全加速网关源站防护详情**

查询 ZoneId 为 'zone-27q0p0bal192' ，GatewayId 为 'mpgw-lbxuhk1oh' 的实例与回源 IP 网段的绑定关系，以及回源 IP 网段详情。

Input: 

```
tccli teo DescribeMultiPathGatewayOriginACL --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh
```

Output: 
```
{
    "Response": {
        "RequestId": "de0a2b4f-df6d-4d2a-ac39-1706cbf8a797",
        "MultiPathGatewayOriginACLInfo": {
            "MultiPathGatewayCurrentOriginACL": {
                "EntireAddresses": {
                    "IPv4": [
                        "11.11.11.11/24"
                    ],
                    "IPv6": [
                        "2001:980:7002:6::/64"
                    ]
                },
                "Version": 3,
                "IsPlaned": "false"
            },
            "MultiPathGatewayNextOriginACL": {
                "Version": 4,
                "EntireAddresses": {
                    "IPv4": [
                        "11.11.11.11/24",
                        "22.22.22.22/24"
                    ],
                    "IPv6": [
                        "2001:980:7002:6::/64"
                    ]
                },
                "AddedAddresses": {
                    "IPv4": [
                        "22.22.22.22/24"
                    ],
                    "IPv6": []
                },
                "RemovedAddresses": {
                    "IPv4": [],
                    "IPv6": []
                },
                "NoChangeAddresses": {
                    "IPv4": [
                        "11.11.11.11/24"
                    ],
                    "IPv6": [
                        "2001:980:7002:6::/64"
                    ]
                }
            }
        }
    }
}
```

