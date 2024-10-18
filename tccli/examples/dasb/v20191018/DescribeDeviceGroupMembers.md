**Example 1: 查询资产组成员列表**



Input: 

```
tccli dasb DescribeDeviceGroupMembers --cli-unfold-argument  \
    --Id 1 \
    --Name 研发主机 \
    --Bound True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DeviceSet": [
            {
                "Id": 1,
                "InstanceId": "abc",
                "Name": "abc",
                "PublicIp": "abc",
                "PrivateIp": "abc",
                "ApCode": "abc",
                "OsName": "abc",
                "Kind": 1,
                "Port": 1,
                "GroupSet": [
                    {
                        "Id": 1,
                        "Name": "abc",
                        "Department": {
                            "Id": "abc",
                            "Name": "abc",
                            "Managers": [
                                "abc"
                            ],
                            "ManagerUsers": [
                                {
                                    "ManagerId": "abc",
                                    "ManagerName": "abc"
                                }
                            ]
                        },
                        "Count": 1
                    }
                ],
                "AccountCount": 1,
                "VpcId": "abc",
                "SubnetId": "abc",
                "Resource": {
                    "ResourceId": "abc",
                    "ApCode": "abc",
                    "SvArgs": "abc",
                    "VpcId": "abc",
                    "Nodes": 1,
                    "RenewFlag": 1,
                    "ExpireTime": "2020-09-22T00:00:00+00:00",
                    "Status": 1,
                    "ResourceName": "abc",
                    "Pid": 1,
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "ProductCode": "abc",
                    "SubProductCode": "abc",
                    "Zone": "abc",
                    "Expired": true,
                    "Deployed": true,
                    "VpcName": "abc",
                    "VpcCidrBlock": "abc",
                    "SubnetId": "abc",
                    "SubnetName": "abc",
                    "CidrBlock": "abc",
                    "PublicIpSet": [
                        "abc"
                    ],
                    "PrivateIpSet": [
                        "abc"
                    ],
                    "ModuleSet": [
                        "abc"
                    ],
                    "UsedNodes": 1,
                    "ExtendPoints": 1,
                    "PackageBandwidth": 1,
                    "PackageNode": 1,
                    "LogDeliveryArgs": "abc",
                    "ClbSet": [
                        {
                            "ClbIp": "abc"
                        }
                    ],
                    "DomainCount": 0,
                    "UsedDomainCount": 1,
                    "Trial": 1
                },
                "Department": {
                    "Id": "abc",
                    "Name": "abc",
                    "Managers": [
                        "abc"
                    ],
                    "ManagerUsers": [
                        {
                            "ManagerId": "abc",
                            "ManagerName": "abc"
                        }
                    ]
                },
                "IpPortSet": [
                    "abc"
                ],
                "DomainId": "abc",
                "DomainName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

