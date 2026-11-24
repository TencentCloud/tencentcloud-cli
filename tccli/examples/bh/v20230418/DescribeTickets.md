**Example 1: 请求示例**



Input: 

```
tccli bh DescribeTickets --cli-unfold-argument  \
    --StatusSet 1 \
    --TicketType 1 \
    --Filters.0.Name test-name \
    --Filters.0.Values value \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TicketSet": [
            {
                "Id": 1,
                "TicketId": "1",
                "TicketType": 1,
                "Acl": {
                    "DeviceGroupSet": [],
                    "Department": {
                        "Id": "",
                        "Name": "",
                        "Managers": []
                    },
                    "Id": 1,
                    "Name": "test-name",
                    "AllowDiskRedirect": true,
                    "AllowClipFileUp": true,
                    "AllowClipFileDown": true,
                    "AllowClipTextUp": true,
                    "AllowClipTextDown": true,
                    "AllowFileUp": true,
                    "MaxFileUpSize": 1,
                    "AllowFileDown": true,
                    "MaxFileDownSize": 1,
                    "AllowAnyAccount": true,
                    "UserSet": [
                        {
                            "Id": 1,
                            "UserName": "test-name",
                            "RealName": "test-name",
                            "Phone": "139******",
                            "Email": "13****@qq.com",
                            "ValidateFrom": "2020-09-22T00:00:00+08:00",
                            "ValidateTo": "2020-09-22T00:00:00+08:00",
                            "GroupSet": [
                                {
                                    "Id": 1,
                                    "Name": "test-name",
                                    "Department": {
                                        "Id": "1",
                                        "Name": "test-name",
                                        "Managers": [
                                            "1"
                                        ],
                                        "ManagerUsers": [
                                            {
                                                "ManagerId": "1",
                                                "ManagerName": "test-name"
                                            }
                                        ]
                                    },
                                    "Count": 1
                                }
                            ],
                            "AuthType": 1,
                            "ValidateTime": "2020-09-22T00:00:00+08:00",
                            "Department": {
                                "Id": "1",
                                "Name": "test-name",
                                "Managers": [
                                    "1"
                                ],
                                "ManagerUsers": [
                                    {
                                        "ManagerId": "1",
                                        "ManagerName": "test-name"
                                    }
                                ]
                            },
                            "DepartmentId": "1",
                            "ActiveStatus": 1,
                            "LockStatus": 1,
                            "Status": "1",
                            "AclVersion": 1
                        }
                    ],
                    "UserGroupSet": [
                        {
                            "Id": 1,
                            "Name": "test-name",
                            "Department": {
                                "Id": "1",
                                "Name": "test-name",
                                "Managers": [
                                    "1"
                                ],
                                "ManagerUsers": [
                                    {
                                        "ManagerId": "1",
                                        "ManagerName": "test-name"
                                    }
                                ]
                            },
                            "Count": 1
                        }
                    ],
                    "DeviceSet": [
                        {
                            "Department": {
                                "Id": "",
                                "Name": "",
                                "Managers": [
                                    "21312434"
                                ]
                            },
                            "Id": 1,
                            "InstanceId": "ins-sdsfdfd",
                            "Name": "test-name",
                            "PublicIp": "10.10.10.10",
                            "PrivateIp": "192.168.0.1",
                            "ApCode": "ap-guangzhou",
                            "OsName": "Linux",
                            "Kind": 1,
                            "Port": 1,
                            "GroupSet": [
                                {
                                    "Id": 1,
                                    "Name": "test-name",
                                    "Count": 1,
                                    "Department": {
                                        "Id": "",
                                        "Name": "",
                                        "Managers": [
                                            "dsfsdfs"
                                        ]
                                    }
                                }
                            ],
                            "AccountCount": 1,
                            "VpcId": "vpc-97hahsd",
                            "SubnetId": "subnet-asdu7ahj",
                            "Resource": {
                                "ResourceId": "bh-saas-0kjaus",
                                "ApCode": "ap-guangzhou",
                                "SvArgs": "sv_cds_dasb_saas_standard_500node",
                                "VpcId": "vpc-sadi8j",
                                "Nodes": 1,
                                "RenewFlag": 1,
                                "ExpireTime": "2020-09-22T00:00:00+08:00",
                                "Status": 1,
                                "ResourceName": "test-name",
                                "Pid": 1,
                                "CreateTime": "2020-09-22T00:00:00+08:00",
                                "ProductCode": "code",
                                "SubProductCode": "code",
                                "Zone": "ap-guangzhou-1",
                                "Expired": true,
                                "Deployed": true,
                                "VpcName": "test-name",
                                "VpcCidrBlock": "192.168.11.0/24",
                                "SubnetId": "subnet-xxxxxx",
                                "SubnetName": "test-name",
                                "CidrBlock": "192.168.11.0/24",
                                "PublicIpSet": [
                                    "10.10.10.10"
                                ],
                                "PrivateIpSet": [
                                    "192.168.0.1"
                                ],
                                "ModuleSet": [
                                    ""
                                ],
                                "UsedNodes": 1,
                                "ExtendPoints": 1,
                                "PackageBandwidth": 1,
                                "PackageNode": 1,
                                "LogDeliveryArgs": ""
                            },
                            "IpPortSet": [
                                ""
                            ]
                        }
                    ],
                    "AccountSet": [
                        "root"
                    ],
                    "CmdTemplateSet": [
                        {
                            "Id": 1,
                            "Name": "test-name",
                            "CmdList": ""
                        }
                    ],
                    "AllowDiskFileUp": true,
                    "AllowDiskFileDown": true,
                    "AllowShellFileUp": true,
                    "AllowShellFileDown": true,
                    "AllowFileDel": true,
                    "ValidateFrom": "2020-09-22T00:00:00+00:00",
                    "ValidateTo": "2020-09-22T00:00:00+00:00",
                    "Status": 1,
                    "AllowAccessCredential": true,
                    "ACTemplateSet": [
                        {
                            "TemplateId": "1",
                            "TemplateName": "test-name",
                            "Description": ""
                        }
                    ],
                    "WhiteCmds": [
                        "pwd"
                    ]
                },
                "StartTime": "2020-09-22T00:00:00+00:00",
                "EndTime": "2020-09-22T00:00:00+00:00",
                "Status": 1,
                "ApplyTime": "2020-09-22T00:00:00+00:00",
                "ApplyUser": 1,
                "ApproveUser": "root",
                "ApproveDesc": "",
                "AclId": 1,
                "ApproveUserSet": [
                    "root"
                ],
                "UpdateTime": "2020-09-22T00:00:00+00:00",
                "Name": "test-name",
                "ApproveTime": "2020-09-22T00:00:00+00:00",
                "DepartmentId": "1",
                "DepartmentSequence": 1,
                "ApplyUserName": "root",
                "ApplyRealName": "root",
                "ApplyTimeVersion": 0
            }
        ],
        "RequestId": "ec7676f4-a498-4ef5-ad68-6678b16e45d7"
    }
}
```

