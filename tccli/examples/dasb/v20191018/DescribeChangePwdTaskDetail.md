**Example 1: 查询改密计划详情**

查询改密计划详情

Input: 

```
tccli dasb DescribeChangePwdTaskDetail --cli-unfold-argument  \
    --OperationId ops-xxx \
    --Filters.0.Name InstanceId \
    --Filters.0.Values ins-xxx \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "Device": {
                    "Id": 1,
                    "InstanceId": "ins-test",
                    "Name": "linux",
                    "PublicIp": "",
                    "PrivateIp": "172.20.0.1",
                    "ApCode": "ap-shanghai-fsi",
                    "OsName": "TencentOS Server 3.1 (TK4)",
                    "Kind": 1,
                    "Port": 22,
                    "IpPortSet": null,
                    "VpcId": "vpc-test",
                    "SubnetId": "subnet-test",
                    "AccountCount": 0,
                    "GroupSet": [
                        {
                            "Id": 1,
                            "Name": "测试",
                            "Department": {
                                "Id": "",
                                "Name": "",
                                "Managers": null,
                                "ManagerUsers": null
                            },
                            "Count": 0
                        }
                    ],
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
                            "1.1.1.1"
                        ],
                        "PrivateIpSet": [
                            "172.0.0.1"
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
                },
                "Account": "worktest",
                "LastChangeStatus": 1
            }
        ],
        "RequestId": "rid-test",
        "TotalCount": 1
    }
}
```

