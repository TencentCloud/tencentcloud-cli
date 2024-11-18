**Example 1: 查询修改密码任务信息**

查询修改密码任务信息

Input: 

```
tccli bh DescribeChangePwdTask --cli-unfold-argument  \
    --Filters.0.Name TaskName \
    --Filters.0.Values task1 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "rid-test-1a2b3c",
        "Tasks": [
            {
                "Id": 1,
                "TaskName": "bhtest102901",
                "OperationId": "ops-ccahmv2z78868363",
                "ChangeMethod": 1,
                "RunAccount": "root",
                "AuthGenerationStrategy": 1,
                "PasswordLength": 12,
                "SmallLetter": 1,
                "BigLetter": 1,
                "Digit": 1,
                "Symbol": "-_#();%~!+=",
                "CompleteNotify": 1,
                "NotifyEmails": [
                    "273****00@qq.com"
                ],
                "FilePassword": "bL69j2RbFoJyOD0UBIpygB3Gv22pM7nIsKlV9ff0LpM=",
                "Type": 4,
                "Period": 0,
                "FirstTime": "2020-12-20T19:51:23+08:00",
                "NextTime": "2020-12-20T19:51:23+08:00",
                "DeviceSet": [
                    {
                        "Id": 10339,
                        "InstanceId": "ins-h8wdh7my",
                        "Name": "Ldap主节点",
                        "PublicIp": "119.29.191.59",
                        "PrivateIp": "192.168.0.12",
                        "ApCode": "ap-guangzhou",
                        "OsName": "CentOS 7.7 64位",
                        "Kind": 1,
                        "Port": 22,
                        "IpPortSet": [
                            "127.0.0.1:80"
                        ],
                        "VpcId": "vpc-q1of50wz",
                        "SubnetId": "subnet-bszyk5a4",
                        "AccountCount": 0,
                        "GroupSet": [
                            {
                                "Id": 4982,
                                "Name": "11",
                                "Department": {
                                    "Id": "",
                                    "Name": "",
                                    "Managers": [],
                                    "ManagerUsers": []
                                },
                                "Count": 0
                            }
                        ],
                        "Resource": {
                            "ResourceId": "bh-saas-ksdf1qbp",
                            "ResourceName": "T-Sec-堡垒机（SaaS型）/专业版",
                            "ApCode": "ap-guangzhou",
                            "Zone": "ap-guangzhou-6",
                            "Pid": 1011353,
                            "SvArgs": "sv_cds_dasb_saas_pro_50node",
                            "PackageBandwidth": 0,
                            "PackageNode": 0,
                            "LogDeliveryArgs": "",
                            "LogDelivery": "",
                            "ProductCode": "p_cds_dasb",
                            "SubProductCode": "sp_cds_dasb_bh_saas_pro",
                            "VpcId": "vpc-q1of50wz",
                            "VpcName": "gordan-test1",
                            "VpcCidrBlock": "192.168.0.0/16",
                            "SubnetId": "subnet-dp102ji4",
                            "SubnetName": "zone6",
                            "CidrBlock": "192.168.24.0/24",
                            "Nodes": 50,
                            "UsedNodes": 48,
                            "PublicIpSet": [
                                "101.33.193.25"
                            ],
                            "PrivateIpSet": [
                                "192.168.24.132",
                                "192.168.24.63"
                            ],
                            "RenewFlag": 0,
                            "CreateTime": "2024-05-07T09:56:31+08:00",
                            "ExpireTime": "2025-10-07T09:56:31+08:00",
                            "Expired": false,
                            "Deployed": true,
                            "Status": 1,
                            "ExtendPoints": 0,
                            "DeployModel": 0,
                            "CdcClusterId": "cluster-262n63e8",
                            "DomainCount": 3,
                            "ClbSet": [
                                {
                                    "ClbIp": "101.33.193.25"
                                },
                                {
                                    "ClbIp": "192.168.24.53"
                                }
                            ],
                            "Trial": 0,
                            "ModuleSet": [],
                            "UsedDomainCount": 3
                        },
                        "DomainId": "net-vpix19hu",
                        "DomainName": "bh-saas-ksdf1qbp default network domain",
                        "Department": {
                            "Id": "1",
                            "Name": "腾讯云",
                            "Managers": [],
                            "ManagerUsers": []
                        },
                        "EnableSSL": 0,
                        "SSLCertName": ""
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

