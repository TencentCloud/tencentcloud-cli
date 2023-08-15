**Example 1: 查询资产列表**

查询资产列表

Input: 

```
tccli dasb DescribeDevices --cli-unfold-argument ```

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
                    "LogDeliveryArgs": "abc"
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
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 根据用户查询有访问权限的资产**

根据用户查询有访问权限的资产

Input: 

```
tccli dasb DescribeDevices --cli-unfold-argument  \
    --AuthorizedUserIdSet 1 7 8 \
    --Name xxx
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
                    "LogDeliveryArgs": "abc"
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
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

