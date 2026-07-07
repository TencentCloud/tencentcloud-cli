**Example 1: 查询实例详情**



Input: 

```
tccli alb DescribeLoadBalancerDetail --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m
```

Output: 
```
{
    "Response": {
        "LoadBalancerDetail": {
            "AccessLogConfig": {
                "LogSetId": "",
                "LogTopicId": ""
            },
            "AddressIpVersion": "IPv4",
            "AddressType": "Intranet",
            "CreateTime": "2025-10-30T12:00:00+08:00",
            "DeletionProtection": {
                "DeletionProtectionEnabled": false,
                "Reason": ""
            },
            "Domain": "alb-f8q2xk9m-vcpcq5puad9vp3xm.gz-tencentalb.com",
            "LoadBalancerBillingConfig": {
                "BandwidthPackageId": "bwp-q8m2x4pa",
                "ChargeType": "POSTPAID_BY_HOUR"
            },
            "LoadBalancerId": "alb-f8q2xk9m",
            "LoadBalancerName": "test-name",
            "LoadBalancerOperationLocks": [],
            "LoadBalancerStatus": "Active",
            "ModificationProtection": {
                "ModificationProtectionEnabled": false,
                "OperatorUin": "",
                "Reason": ""
            },
            "SecurityGroupIds": [],
            "Tags": [],
            "VpcId": "vpc-92hffaxb",
            "ZoneMappings": [
                {
                    "LoadBalancerAddress": {
                        "IPv4Address": [
                            {
                                "Address": "172.16.80.118",
                                "AddressId": ""
                            }
                        ],
                        "IPv6Address": []
                    },
                    "Status": "Active",
                    "SubnetId": "subnet-bi75pogm",
                    "ZoneId": "ap-guangzhou-3"
                },
                {
                    "LoadBalancerAddress": {
                        "IPv4Address": [
                            {
                                "Address": "172.16.32.181",
                                "AddressId": ""
                            }
                        ],
                        "IPv6Address": []
                    },
                    "Status": "Active",
                    "SubnetId": "subnet-bi75pogm",
                    "ZoneId": "ap-guangzhou-2"
                }
            ]
        },
        "RequestId": "f87fe97c-d4b3-4c1e-9256-36af067be287"
    }
}
```

