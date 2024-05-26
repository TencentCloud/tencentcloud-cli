**Example 1: 查询修改密码任务信息**

查询修改密码任务信息

Input: 

```
tccli dasb DescribeChangePwdTask --cli-unfold-argument  \
    --Filters.0.Name TaskName \
    --Filters.0.Values task1 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "rid-test",
        "Tasks": [
            {
                "Id": 1,
                "TaskName": "test-xxx",
                "OperationId": "ops-xxx",
                "ChangeMethod": 1,
                "RunAccount": "root",
                "AuthGenerationStrategy": 1,
                "PasswordLength": 12,
                "SmallLetter": 1,
                "BigLetter": 1,
                "Digit": 1,
                "Symbol": "",
                "CompleteNotify": 1,
                "NotifyEmails": [
                    "11323@qq.com"
                ],
                "FilePassword": "xxx",
                "Type": 4,
                "Period": 0,
                "FirstTime": null,
                "NextTime": null,
                "DeviceSet": [
                    {
                        "Id": 1,
                        "InstanceId": "ins-a3dvgvte",
                        "Name": "可用-预发标准版-linux",
                        "PublicIp": "",
                        "PrivateIp": "172.20.0.17",
                        "ApCode": "ap-shanghai-fsi",
                        "OsName": "TencentOS Server 3.1 (TK4)",
                        "Kind": 1,
                        "Port": 22,
                        "IpPortSet": null,
                        "VpcId": "vpc-test",
                        "SubnetId": "subnet-test",
                        "AccountCount": 0,
                        "GroupSet": [],
                        "Resource": {
                            "ResourceId": "bh-saas-test",
                            "ResourceName": "T-Sec-堡垒机（SaaS型）/专业版",
                            "ApCode": "ap-shanghai-fsi",
                            "Zone": "ap-shanghai-fsi-1",
                            "Pid": 10,
                            "SvArgs": "sv_cds_dasb_saas_ex_pro_xxx",
                            "PackageBandwidth": 0,
                            "PackageNode": 0,
                            "LogDeliveryArgs": "",
                            "ProductCode": "p_cds_dasb",
                            "SubProductCode": "sp_cds_dasb_bh_saas_pro",
                            "VpcId": "vpc-test",
                            "VpcName": "Default-VPC",
                            "VpcCidrBlock": "172.20.0.0/16",
                            "SubnetId": "subnet-test",
                            "SubnetName": "1qu",
                            "CidrBlock": "172.20.50.0/24",
                            "Nodes": 50,
                            "UsedNodes": 2,
                            "PublicIpSet": [
                                "101.35.32.101"
                            ],
                            "PrivateIpSet": [
                                "172.20.50.50"
                            ],
                            "RenewFlag": 2,
                            "CreateTime": "2024-04-28T11:00:59+08:00",
                            "ExpireTime": "2024-05-28T11:00:59+08:00",
                            "Expired": false,
                            "Deployed": true,
                            "Status": 1,
                            "ExtendPoints": 0,
                            "ModuleSet": []
                        },
                        "Department": {
                            "Id": "1",
                            "Name": "总部",
                            "Managers": null,
                            "ManagerUsers": null
                        }
                    }
                ],
                "AccountSet": [
                    "test042303",
                    "test042304",
                    "test042305",
                    "test092702"
                ],
                "Department": {
                    "Id": "1",
                    "Name": "总部",
                    "Managers": null,
                    "ManagerUsers": null
                }
            }
        ],
        "TotalCount": 1
    }
}
```

