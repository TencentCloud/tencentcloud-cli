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
                "InstanceId": "Ins-89j1",
                "Name": "运维主机",
                "PublicIp": "192.0.2.123",
                "PrivateIp": "10.0.0.123",
                "ApCode": "ap-guangzhou",
                "OsName": "linux",
                "Kind": 1,
                "Port": 1,
                "GroupSet": [
                    {
                        "Id": 1,
                        "Name": "group1213",
                        "Department": {
                            "Id": "dept1415",
                            "Name": "deptName1617",
                            "Managers": [
                                "manager1819"
                            ],
                            "ManagerUsers": [
                                {
                                    "ManagerId": "managerId2021",
                                    "ManagerName": "managerName2223"
                                }
                            ]
                        },
                        "Count": 1
                    }
                ],
                "AccountCount": 1,
                "VpcId": "vpc-2425",
                "SubnetId": "subnet-2627",
                "Resource": {
                    "ResourceId": "bh-saas-resource",
                    "ApCode": "ap3031",
                    "SvArgs": "sv3233",
                    "VpcId": "vpc3435",
                    "Nodes": 1,
                    "RenewFlag": 1,
                    "ExpireTime": "2020-09-22T00:00:00+00:00",
                    "Status": 1,
                    "ResourceName": "resource3637",
                    "Pid": 1,
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "ProductCode": "product3839",
                    "SubProductCode": "subproduct4041",
                    "Zone": "zone4243",
                    "Expired": true,
                    "Deployed": true,
                    "VpcName": "vpc-4445",
                    "VpcCidrBlock": "10.0.0.0/16",
                    "SubnetId": "subnet-4647",
                    "SubnetName": "subnetName4849",
                    "CidrBlock": "10.0.1.0/24",
                    "PublicIpSet": [
                        "192.0.2.123"
                    ],
                    "PrivateIpSet": [
                        "10.0.0.123"
                    ],
                    "ModuleSet": [
                        "module5051"
                    ],
                    "UsedNodes": 1,
                    "ExtendPoints": 1,
                    "PackageBandwidth": 1,
                    "PackageNode": 1,
                    "LogDeliveryArgs": "log5253",
                    "ClbSet": [
                        {
                            "ClbIp": "192.0.2.123"
                        }
                    ],
                    "DomainCount": 1,
                    "UsedDomainCount": 1,
                    "Trial": 1,
                    "LogDelivery": "log5455",
                    "CdcClusterId": "cdc5657",
                    "DeployModel": 1
                },
                "Department": {
                    "Id": "dept6061",
                    "Name": "deptName6263",
                    "Managers": [
                        "manager6465"
                    ],
                    "ManagerUsers": [
                        {
                            "ManagerId": "managerId6667",
                            "ManagerName": "managerName6869"
                        }
                    ]
                },
                "IpPortSet": [
                    "192.0.2.123:80"
                ],
                "DomainId": "net-default",
                "DomainName": "默认网络域",
                "EnableSSL": 0,
                "SSLCertName": "bh-test-cert"
            }
        ],
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

