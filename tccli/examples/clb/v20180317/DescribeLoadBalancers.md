**Example 1: 根据负载均衡实例ID来查询**



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
                "LoadBalancerId": "lb-rbw5****",
                "LoadBalancerName": "test_LB_****",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerDomain": "",
                "LoadBalancerVips": [
                    "119.***.***.51"
                ],
                "AddressIPv6": null,
                "AddressIPVersion": "ipv4",
                "IPv6Mode": null,
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2023-12-27 15:53:46",
                "StatusTime": "2024-01-22 19:58:03",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "VpcId": "vpc-1y****83",
                "NumericalVpcId": 1111113,
                "TargetRegionInfo": {
                    "Region": "ap-guangzhou",
                    "VpcId": "vpc-1y****83"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [
                    {
                        "TagKey": "key-****",
                        "TagValue": "value-****"
                    }
                ],
                "MasterZone": {
                    "ZoneId": 100003,
                    "Zone": "ap-guangzhou-3",
                    "ZoneName": "广州三区",
                    "ZoneRegion": "ap-guangzhou",
                    "LocalZone": false,
                    "EdgeZone": false
                },
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2024-01-27 15:53:46",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 5,
                    "BandwidthpkgSubType": "BGP"
                },
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
                "ClusterTag": null,
                "LocalBgp": false,
                "MixIpTarget": false,
                "Zones": null,
                "NfvInfo": "",
                "HealthLogSetId": "",
                "HealthLogTopicId": "",
                "ClusterIds": null,
                "AttributeFlags": [
                    "SharedLimitFlag"
                ],
                "VipIsp": "BGP",
                "Egress": ""
            }
        ],
        "RequestId": "b0e9e810-01cc-4c12-8bd2-ca0a2ab1b976"
    }
}
```

**Example 2: 根据负载均衡的标签键值对过滤查询**



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
                "LoadBalancerId": "lb-rbw5****",
                "LoadBalancerName": "test_LB_****",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerDomain": "",
                "LoadBalancerVips": [
                    "119.***.***.51"
                ],
                "AddressIPv6": null,
                "AddressIPVersion": "ipv4",
                "IPv6Mode": null,
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2023-12-27 15:53:46",
                "StatusTime": "2024-01-22 19:58:03",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "VpcId": "vpc-1y****83",
                "NumericalVpcId": 1111113,
                "TargetRegionInfo": {
                    "Region": "ap-guangzhou",
                    "VpcId": "vpc-1y****83"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [
                    {
                        "TagKey": "key-****",
                        "TagValue": "value-****"
                    }
                ],
                "MasterZone": {
                    "ZoneId": 100003,
                    "Zone": "ap-guangzhou-3",
                    "ZoneName": "广州三区",
                    "ZoneRegion": "ap-guangzhou",
                    "LocalZone": false,
                    "EdgeZone": false
                },
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2024-01-27 15:53:46",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 5,
                    "BandwidthpkgSubType": "BGP"
                },
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
                "ClusterTag": null,
                "LocalBgp": false,
                "MixIpTarget": false,
                "Zones": null,
                "NfvInfo": "",
                "HealthLogSetId": "",
                "HealthLogTopicId": "",
                "ClusterIds": null,
                "AttributeFlags": [
                    "SharedLimitFlag"
                ],
                "VipIsp": "BGP",
                "Egress": ""
            }
        ],
        "RequestId": "b0e9e810-01cc-4c12-8bd2-ca0a2ab1b976"
    }
}
```

**Example 3: 查询后端绑定了指定内网IP的机器的负载均衡**

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
                "LoadBalancerId": "lb-9vpm****",
                "LoadBalancerName": "lb-test-****-1227",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerDomain": "",
                "LoadBalancerVips": [
                    "119.***.***.51"
                ],
                "AddressIPv6": null,
                "AddressIPVersion": "ipv4",
                "IPv6Mode": null,
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2023-12-27 15:53:46",
                "StatusTime": "2024-01-22 19:58:03",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "VpcId": "vpc-1y****83",
                "NumericalVpcId": 1111113,
                "TargetRegionInfo": {
                    "Region": "ap-guangzhou",
                    "VpcId": "vpc-1y****83"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [
                    {
                        "TagKey": "key-****",
                        "TagValue": "value-****"
                    }
                ],
                "MasterZone": {
                    "ZoneId": 100003,
                    "Zone": "ap-guangzhou-3",
                    "ZoneName": "广州三区",
                    "ZoneRegion": "ap-guangzhou",
                    "LocalZone": false,
                    "EdgeZone": false
                },
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2024-01-27 15:53:46",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 5,
                    "BandwidthpkgSubType": "BGP"
                },
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
                "ClusterTag": null,
                "LocalBgp": false,
                "MixIpTarget": false,
                "Zones": null,
                "NfvInfo": "",
                "HealthLogSetId": "",
                "HealthLogTopicId": "",
                "ClusterIds": null,
                "AttributeFlags": [
                    "SharedLimitFlag"
                ],
                "VipIsp": "BGP",
                "Egress": ""
            }
        ],
        "RequestId": "b0e9e810-01cc-4c12-8bd2-ca0a2ab1b976"
    }
}
```

**Example 4: 根据名称、域名、VIP多个字段模糊查询负载均衡实例**



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
                "LoadBalancerId": "lb-9vpm****",
                "LoadBalancerName": "test_LB_****",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerDomain": "",
                "LoadBalancerVips": [
                    "119.***.***.51"
                ],
                "AddressIPv6": null,
                "AddressIPVersion": "ipv4",
                "IPv6Mode": null,
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2023-12-27 15:53:46",
                "StatusTime": "2024-01-22 19:58:03",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "VpcId": "vpc-1y****83",
                "NumericalVpcId": 1111113,
                "TargetRegionInfo": {
                    "Region": "ap-guangzhou",
                    "VpcId": "vpc-1y****83"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [
                    {
                        "TagKey": "key-****",
                        "TagValue": "value-****"
                    }
                ],
                "MasterZone": {
                    "ZoneId": 100003,
                    "Zone": "ap-guangzhou-3",
                    "ZoneName": "广州三区",
                    "ZoneRegion": "ap-guangzhou",
                    "LocalZone": false,
                    "EdgeZone": false
                },
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2024-01-27 15:53:46",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 5,
                    "BandwidthpkgSubType": "BGP"
                },
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
                "ClusterTag": null,
                "LocalBgp": false,
                "MixIpTarget": false,
                "Zones": null,
                "NfvInfo": "",
                "HealthLogSetId": "",
                "HealthLogTopicId": "",
                "ClusterIds": null,
                "AttributeFlags": [
                    "SharedLimitFlag"
                ],
                "VipIsp": "BGP",
                "Egress": ""
            }
        ],
        "RequestId": "b0e9e810-01cc-4c12-8bd2-ca0a2ab1b976"
    }
}
```

**Example 5: 根据负载均衡类型、所属项目、负载均衡名称、负载均衡实例的vip来查询**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --ProjectId 0 \
    --LoadBalancerType OPEN \
    --LoadBalancerVips 119.***.***.51 \
    --LoadBalancerName test_LB
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-rbw5****",
                "LoadBalancerName": "test_LB_****",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerDomain": "",
                "LoadBalancerVips": [
                    "119.***.***.51"
                ],
                "AddressIPv6": null,
                "AddressIPVersion": "ipv4",
                "IPv6Mode": null,
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2023-12-27 15:53:46",
                "StatusTime": "2024-01-22 19:58:03",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "VpcId": "vpc-1y****83",
                "NumericalVpcId": 1111113,
                "TargetRegionInfo": {
                    "Region": "ap-guangzhou",
                    "VpcId": "vpc-1y****83"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [
                    {
                        "TagKey": "key-****",
                        "TagValue": "value-****"
                    }
                ],
                "MasterZone": {
                    "ZoneId": 100003,
                    "Zone": "ap-guangzhou-3",
                    "ZoneName": "广州三区",
                    "ZoneRegion": "ap-guangzhou",
                    "LocalZone": false,
                    "EdgeZone": false
                },
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2024-01-27 15:53:46",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 5,
                    "BandwidthpkgSubType": "BGP"
                },
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
                "ClusterTag": null,
                "LocalBgp": false,
                "MixIpTarget": false,
                "Zones": null,
                "NfvInfo": "",
                "HealthLogSetId": "",
                "HealthLogTopicId": "",
                "ClusterIds": null,
                "AttributeFlags": [
                    "SharedLimitFlag"
                ],
                "VipIsp": "BGP",
                "Egress": ""
            }
        ],
        "RequestId": "b0e9e810-01cc-4c12-8bd2-ca0a2ab1b976"
    }
}
```

