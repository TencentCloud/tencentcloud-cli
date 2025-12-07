**Example 1: 指定的证书ID有关联到负载均衡**



Input: 

```
tccli clb DescribeLoadBalancerListByCertId --cli-unfold-argument  \
    --CertIds Rrsw4nIA
```

Output: 
```
{
    "Response": {
        "CertSet": [
            {
                "CertId": "Rrsw4nIA",
                "LoadBalancers": [
                    {
                        "LoadBalancerId": "lb-8vzdrrfr",
                        "LoadBalancerName": "prd02-ai-bj-ape-ingress",
                        "Forward": 1,
                        "Domain": "",
                        "LoadBalancerDomain": "",
                        "LoadBalancerVips": [
                            "172.16.26.14"
                        ],
                        "AddressIPv6": null,
                        "AddressIPVersion": "ipv4",
                        "IPv6Mode": null,
                        "LoadBalancerType": "INTERNAL",
                        "Status": 1,
                        "CreateTime": "2024-12-11 16:37:29",
                        "StatusTime": "2025-04-27 13:37:46",
                        "ProjectId": 0,
                        "OpenBgp": 0,
                        "Snat": false,
                        "Isolation": 0,
                        "Log": "",
                        "AnycastZone": "",
                        "VpcId": "vpc-6cv6qg1u",
                        "NumericalVpcId": 9356678,
                        "TargetRegionInfo": {
                            "Region": "ap-beijing",
                            "VpcId": "vpc-6cv3qr1u",
                            "NumericalVpcId": 9356678
                        },
                        "SubnetId": "",
                        "SecureGroups": [],
                        "Tags": [
                            {
                                "TagKey": "tke-createdBy-flag",
                                "TagValue": "yes"
                            },
                            {
                                "TagKey": "tke-clusterId",
                                "TagValue": "cls-27punli3"
                            }
                        ],
                        "MasterZone": null,
                        "BackupZoneSet": null,
                        "IsolatedTime": null,
                        "ExpireTime": null,
                        "ChargeType": null,
                        "NetworkAttributes": null,
                        "PrepaidAttributes": null,
                        "ExtraInfo": null,
                        "LogSetId": "",
                        "LogTopicId": "",
                        "LoadBalancerPassToTarget": false,
                        "IsDDos": false,
                        "ConfigId": "",
                        "ExclusiveCluster": {
                            "L4Clusters": null,
                            "L7Clusters": null,
                            "ClassicalCluster": null
                        },
                        "SnatPro": false,
                        "SnatIps": [],
                        "IsBlock": false,
                        "IsBlockTime": "",
                        "SlaType": "",
                        "Exclusive": null,
                        "ClusterTag": null,
                        "LocalBgp": false,
                        "MixIpTarget": false,
                        "Zones": null,
                        "NfvInfo": "",
                        "HealthLogSetId": "",
                        "HealthLogTopicId": "",
                        "ClusterIds": null,
                        "AttributeFlags": [
                            "SgInTgw",
                            "SharedLimitFlag"
                        ],
                        "Egress": "",
                        "VipIsp": "INTERNAL"
                    }
                ]
            }
        ],
        "RequestId": "7718d187-7684-4294-324b-1e13009d75f6"
    }
}
```

**Example 2: 指定的证书ID没有关联到任何负载均衡**



Input: 

```
tccli clb DescribeLoadBalancerListByCertId --cli-unfold-argument  \
    --CertIds RwFAfr8Y
```

Output: 
```
{
    "Response": {
        "CertSet": [
            {
                "CertId": "RwFAfr8Y",
                "LoadBalancers": []
            }
        ],
        "RequestId": "fe6059b5-faa6-4f21-92a1-0c9ee5df5e54"
    }
}
```

