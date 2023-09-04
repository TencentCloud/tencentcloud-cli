**Example 1: 查询后端绑定了指定内网IP的机器的负载均衡**

查询绑定了内网IP为172.26.0.11的后端服务的负载均衡实例。

Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --BackendPrivateIps 172.26.0.11 \
    --WithRs 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "abc",
                "LoadBalancerName": "abc",
                "LoadBalancerType": "abc",
                "Forward": 1,
                "Domain": "abc",
                "LoadBalancerVips": [
                    "abc"
                ],
                "Status": 1,
                "CreateTime": "abc",
                "StatusTime": "abc",
                "ProjectId": 1,
                "VpcId": "abc",
                "OpenBgp": 1,
                "Snat": true,
                "Isolation": 1,
                "Log": "abc",
                "SubnetId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "SecureGroups": [
                    "abc"
                ],
                "TargetRegionInfo": {
                    "Region": "abc",
                    "VpcId": "abc"
                },
                "AnycastZone": "abc",
                "AddressIPVersion": "abc",
                "NumericalVpcId": 1,
                "VipIsp": "abc",
                "MasterZone": {
                    "ZoneId": 1,
                    "Zone": "abc",
                    "ZoneName": "abc",
                    "ZoneRegion": "abc",
                    "LocalZone": true,
                    "EdgeZone": true
                },
                "BackupZoneSet": [
                    {
                        "ZoneId": 1,
                        "Zone": "abc",
                        "ZoneName": "abc",
                        "ZoneRegion": "abc",
                        "LocalZone": true,
                        "EdgeZone": true
                    }
                ],
                "IsolatedTime": "abc",
                "ExpireTime": "abc",
                "ChargeType": "abc",
                "NetworkAttributes": {
                    "InternetChargeType": "abc",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthpkgSubType": "abc"
                },
                "PrepaidAttributes": {
                    "RenewFlag": "abc",
                    "Period": 0
                },
                "LogSetId": "abc",
                "LogTopicId": "abc",
                "AddressIPv6": "abc",
                "ExtraInfo": {
                    "ZhiTong": true,
                    "TgwGroupName": "abc"
                },
                "IsDDos": true,
                "ConfigId": "abc",
                "LoadBalancerPassToTarget": true,
                "ExclusiveCluster": {
                    "L4Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "L7Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "ClassicalCluster": {
                        "ClusterId": "abc",
                        "ClusterName": "abc",
                        "Zone": "abc"
                    }
                },
                "IPv6Mode": "abc",
                "SnatPro": true,
                "SnatIps": [
                    {
                        "SubnetId": "abc",
                        "Ip": "abc"
                    }
                ],
                "SlaType": "abc",
                "IsBlock": true,
                "IsBlockTime": "abc",
                "LocalBgp": true,
                "ClusterTag": "abc",
                "MixIpTarget": true,
                "Zones": [
                    "abc"
                ],
                "NfvInfo": "abc",
                "HealthLogSetId": "abc",
                "HealthLogTopicId": "abc",
                "ClusterIds": [
                    "abc"
                ],
                "AttributeFlags": [
                    "abc"
                ],
                "LoadBalancerDomain": "abc",
                "Egress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 根据名称、域名、VIP多个字段模糊查询负载均衡实例**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --SearchKey test_LB
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "abc",
                "LoadBalancerName": "abc",
                "LoadBalancerType": "abc",
                "Forward": 1,
                "Domain": "abc",
                "LoadBalancerVips": [
                    "abc"
                ],
                "Status": 1,
                "CreateTime": "abc",
                "StatusTime": "abc",
                "ProjectId": 1,
                "VpcId": "abc",
                "OpenBgp": 1,
                "Snat": true,
                "Isolation": 1,
                "Log": "abc",
                "SubnetId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "SecureGroups": [
                    "abc"
                ],
                "TargetRegionInfo": {
                    "Region": "abc",
                    "VpcId": "abc"
                },
                "AnycastZone": "abc",
                "AddressIPVersion": "abc",
                "NumericalVpcId": 1,
                "VipIsp": "abc",
                "MasterZone": {
                    "ZoneId": 1,
                    "Zone": "abc",
                    "ZoneName": "abc",
                    "ZoneRegion": "abc",
                    "LocalZone": true,
                    "EdgeZone": true
                },
                "BackupZoneSet": [
                    {
                        "ZoneId": 1,
                        "Zone": "abc",
                        "ZoneName": "abc",
                        "ZoneRegion": "abc",
                        "LocalZone": true,
                        "EdgeZone": true
                    }
                ],
                "IsolatedTime": "abc",
                "ExpireTime": "abc",
                "ChargeType": "abc",
                "NetworkAttributes": {
                    "InternetChargeType": "abc",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthpkgSubType": "abc"
                },
                "PrepaidAttributes": {
                    "RenewFlag": "abc",
                    "Period": 0
                },
                "LogSetId": "abc",
                "LogTopicId": "abc",
                "AddressIPv6": "abc",
                "ExtraInfo": {
                    "ZhiTong": true,
                    "TgwGroupName": "abc"
                },
                "IsDDos": true,
                "ConfigId": "abc",
                "LoadBalancerPassToTarget": true,
                "ExclusiveCluster": {
                    "L4Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "L7Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "ClassicalCluster": {
                        "ClusterId": "abc",
                        "ClusterName": "abc",
                        "Zone": "abc"
                    }
                },
                "IPv6Mode": "abc",
                "SnatPro": true,
                "SnatIps": [
                    {
                        "SubnetId": "abc",
                        "Ip": "abc"
                    }
                ],
                "SlaType": "abc",
                "IsBlock": true,
                "IsBlockTime": "abc",
                "LocalBgp": true,
                "ClusterTag": "abc",
                "MixIpTarget": true,
                "Zones": [
                    "abc"
                ],
                "NfvInfo": "abc",
                "HealthLogSetId": "abc",
                "HealthLogTopicId": "abc",
                "ClusterIds": [
                    "abc"
                ],
                "AttributeFlags": [
                    "abc"
                ],
                "LoadBalancerDomain": "abc",
                "Egress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 3: 根据负载均衡实例ID来查询**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --LoadBalancerIds lb-rbw5****
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "abc",
                "LoadBalancerName": "abc",
                "LoadBalancerType": "abc",
                "Forward": 1,
                "Domain": "abc",
                "LoadBalancerVips": [
                    "abc"
                ],
                "Status": 1,
                "CreateTime": "abc",
                "StatusTime": "abc",
                "ProjectId": 1,
                "VpcId": "abc",
                "OpenBgp": 1,
                "Snat": true,
                "Isolation": 1,
                "Log": "abc",
                "SubnetId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "SecureGroups": [
                    "abc"
                ],
                "TargetRegionInfo": {
                    "Region": "abc",
                    "VpcId": "abc"
                },
                "AnycastZone": "abc",
                "AddressIPVersion": "abc",
                "NumericalVpcId": 1,
                "VipIsp": "abc",
                "MasterZone": {
                    "ZoneId": 1,
                    "Zone": "abc",
                    "ZoneName": "abc",
                    "ZoneRegion": "abc",
                    "LocalZone": true,
                    "EdgeZone": true
                },
                "BackupZoneSet": [
                    {
                        "ZoneId": 1,
                        "Zone": "abc",
                        "ZoneName": "abc",
                        "ZoneRegion": "abc",
                        "LocalZone": true,
                        "EdgeZone": true
                    }
                ],
                "IsolatedTime": "abc",
                "ExpireTime": "abc",
                "ChargeType": "abc",
                "NetworkAttributes": {
                    "InternetChargeType": "abc",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthpkgSubType": "abc"
                },
                "PrepaidAttributes": {
                    "RenewFlag": "abc",
                    "Period": 0
                },
                "LogSetId": "abc",
                "LogTopicId": "abc",
                "AddressIPv6": "abc",
                "ExtraInfo": {
                    "ZhiTong": true,
                    "TgwGroupName": "abc"
                },
                "IsDDos": true,
                "ConfigId": "abc",
                "LoadBalancerPassToTarget": true,
                "ExclusiveCluster": {
                    "L4Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "L7Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "ClassicalCluster": {
                        "ClusterId": "abc",
                        "ClusterName": "abc",
                        "Zone": "abc"
                    }
                },
                "IPv6Mode": "abc",
                "SnatPro": true,
                "SnatIps": [
                    {
                        "SubnetId": "abc",
                        "Ip": "abc"
                    }
                ],
                "SlaType": "abc",
                "IsBlock": true,
                "IsBlockTime": "abc",
                "LocalBgp": true,
                "ClusterTag": "abc",
                "MixIpTarget": true,
                "Zones": [
                    "abc"
                ],
                "NfvInfo": "abc",
                "HealthLogSetId": "abc",
                "HealthLogTopicId": "abc",
                "ClusterIds": [
                    "abc"
                ],
                "AttributeFlags": [
                    "abc"
                ],
                "LoadBalancerDomain": "abc",
                "Egress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 4: 根据负载均衡类型、所属项目、负载均衡名称、负载均衡实例的vip来查询**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --ProjectId 0 \
    --LoadBalancerType OPEN \
    --LoadBalancerVips XX.XX.XX.XX \
    --LoadBalancerName test_LB
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "abc",
                "LoadBalancerName": "abc",
                "LoadBalancerType": "abc",
                "Forward": 1,
                "Domain": "abc",
                "LoadBalancerVips": [
                    "abc"
                ],
                "Status": 1,
                "CreateTime": "abc",
                "StatusTime": "abc",
                "ProjectId": 1,
                "VpcId": "abc",
                "OpenBgp": 1,
                "Snat": true,
                "Isolation": 1,
                "Log": "abc",
                "SubnetId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "SecureGroups": [
                    "abc"
                ],
                "TargetRegionInfo": {
                    "Region": "abc",
                    "VpcId": "abc"
                },
                "AnycastZone": "abc",
                "AddressIPVersion": "abc",
                "NumericalVpcId": 1,
                "VipIsp": "abc",
                "MasterZone": {
                    "ZoneId": 1,
                    "Zone": "abc",
                    "ZoneName": "abc",
                    "ZoneRegion": "abc",
                    "LocalZone": true,
                    "EdgeZone": true
                },
                "BackupZoneSet": [
                    {
                        "ZoneId": 1,
                        "Zone": "abc",
                        "ZoneName": "abc",
                        "ZoneRegion": "abc",
                        "LocalZone": true,
                        "EdgeZone": true
                    }
                ],
                "IsolatedTime": "abc",
                "ExpireTime": "abc",
                "ChargeType": "abc",
                "NetworkAttributes": {
                    "InternetChargeType": "abc",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthpkgSubType": "abc"
                },
                "PrepaidAttributes": {
                    "RenewFlag": "abc",
                    "Period": 0
                },
                "LogSetId": "abc",
                "LogTopicId": "abc",
                "AddressIPv6": "abc",
                "ExtraInfo": {
                    "ZhiTong": true,
                    "TgwGroupName": "abc"
                },
                "IsDDos": true,
                "ConfigId": "abc",
                "LoadBalancerPassToTarget": true,
                "ExclusiveCluster": {
                    "L4Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "L7Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "ClassicalCluster": {
                        "ClusterId": "abc",
                        "ClusterName": "abc",
                        "Zone": "abc"
                    }
                },
                "IPv6Mode": "abc",
                "SnatPro": true,
                "SnatIps": [
                    {
                        "SubnetId": "abc",
                        "Ip": "abc"
                    }
                ],
                "SlaType": "abc",
                "IsBlock": true,
                "IsBlockTime": "abc",
                "LocalBgp": true,
                "ClusterTag": "abc",
                "MixIpTarget": true,
                "Zones": [
                    "abc"
                ],
                "NfvInfo": "abc",
                "HealthLogSetId": "abc",
                "HealthLogTopicId": "abc",
                "ClusterIds": [
                    "abc"
                ],
                "AttributeFlags": [
                    "abc"
                ],
                "LoadBalancerDomain": "abc",
                "Egress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 5: 根据负载均衡的标签键值对过滤查询**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --ProjectId 0 \
    --LoadBalancerType OPEN \
    --Filters.0.Values test_tag_value2 test_tag_value1 \
    --Filters.0.Name tag:test_tag_key \
    --LoadBalancerName test_LB
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "abc",
                "LoadBalancerName": "abc",
                "LoadBalancerType": "abc",
                "Forward": 1,
                "Domain": "abc",
                "LoadBalancerVips": [
                    "abc"
                ],
                "Status": 1,
                "CreateTime": "abc",
                "StatusTime": "abc",
                "ProjectId": 1,
                "VpcId": "abc",
                "OpenBgp": 1,
                "Snat": true,
                "Isolation": 1,
                "Log": "abc",
                "SubnetId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "SecureGroups": [
                    "abc"
                ],
                "TargetRegionInfo": {
                    "Region": "abc",
                    "VpcId": "abc"
                },
                "AnycastZone": "abc",
                "AddressIPVersion": "abc",
                "NumericalVpcId": 1,
                "VipIsp": "abc",
                "MasterZone": {
                    "ZoneId": 1,
                    "Zone": "abc",
                    "ZoneName": "abc",
                    "ZoneRegion": "abc",
                    "LocalZone": true,
                    "EdgeZone": true
                },
                "BackupZoneSet": [
                    {
                        "ZoneId": 1,
                        "Zone": "abc",
                        "ZoneName": "abc",
                        "ZoneRegion": "abc",
                        "LocalZone": true,
                        "EdgeZone": true
                    }
                ],
                "IsolatedTime": "abc",
                "ExpireTime": "abc",
                "ChargeType": "abc",
                "NetworkAttributes": {
                    "InternetChargeType": "abc",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthpkgSubType": "abc"
                },
                "PrepaidAttributes": {
                    "RenewFlag": "abc",
                    "Period": 0
                },
                "LogSetId": "abc",
                "LogTopicId": "abc",
                "AddressIPv6": "abc",
                "ExtraInfo": {
                    "ZhiTong": true,
                    "TgwGroupName": "abc"
                },
                "IsDDos": true,
                "ConfigId": "abc",
                "LoadBalancerPassToTarget": true,
                "ExclusiveCluster": {
                    "L4Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "L7Clusters": [
                        {
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "Zone": "abc"
                        }
                    ],
                    "ClassicalCluster": {
                        "ClusterId": "abc",
                        "ClusterName": "abc",
                        "Zone": "abc"
                    }
                },
                "IPv6Mode": "abc",
                "SnatPro": true,
                "SnatIps": [
                    {
                        "SubnetId": "abc",
                        "Ip": "abc"
                    }
                ],
                "SlaType": "abc",
                "IsBlock": true,
                "IsBlockTime": "abc",
                "LocalBgp": true,
                "ClusterTag": "abc",
                "MixIpTarget": true,
                "Zones": [
                    "abc"
                ],
                "NfvInfo": "abc",
                "HealthLogSetId": "abc",
                "HealthLogTopicId": "abc",
                "ClusterIds": [
                    "abc"
                ],
                "AttributeFlags": [
                    "abc"
                ],
                "LoadBalancerDomain": "abc",
                "Egress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

