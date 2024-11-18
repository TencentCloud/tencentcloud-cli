**Example 1: 查询改密计划详情**

查询改密计划详情

Input: 

```
tccli bh DescribeChangePwdTaskDetail --cli-unfold-argument  \
    --OperationId ops-bhtest \
    --DepartmentId 1 \
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
                    "Id": 11292,
                    "InstanceId": "ins-gggllp1g",
                    "Name": "redis8.5_OS 8.5",
                    "PublicIp": "175.178.7.198",
                    "PrivateIp": "192.168.0.11",
                    "ApCode": "ap-guangzhou",
                    "OsName": "CentOS 8.5 64位",
                    "Kind": 1,
                    "Port": 22,
                    "IpPortSet": [
                        "127.0.0.1:20"
                    ],
                    "VpcId": "vpc-q1of50wz",
                    "SubnetId": "subnet-bszyk5a4",
                    "AccountCount": 0,
                    "GroupSet": [],
                    "Resource": {
                        "ResourceId": "bh-saas-tyxci8sl",
                        "ResourceName": "T-Sec-堡垒机（SaaS型）/专业版",
                        "ApCode": "ap-guangzhou",
                        "Zone": "ap-guangzhou-3",
                        "Pid": 1011353,
                        "SvArgs": "sv_cds_dasb_saas_pro_50node",
                        "PackageBandwidth": 0,
                        "PackageNode": 0,
                        "LogDeliveryArgs": "sv_cds_dasb_saas_exp_log_delivery",
                        "LogDelivery": "sv_cds_dasb_saas_exp_log_delivery",
                        "ProductCode": "p_cds_dasb",
                        "SubProductCode": "sp_cds_dasb_bh_saas_pro",
                        "VpcId": "vpc-q1of50wz",
                        "VpcName": "gordan-test1",
                        "VpcCidrBlock": "192.168.0.0/16",
                        "SubnetId": "subnet-ebqdl3f4",
                        "SubnetName": "test1",
                        "CidrBlock": "192.168.1.0/24",
                        "Nodes": 50,
                        "UsedNodes": 38,
                        "PublicIpSet": [
                            "111.230.121.212"
                        ],
                        "PrivateIpSet": [
                            "192.168.1.12",
                            "192.168.1.49"
                        ],
                        "RenewFlag": 0,
                        "CreateTime": "2024-02-27T10:47:58+08:00",
                        "ExpireTime": "2030-09-28T10:47:58+08:00",
                        "Expired": false,
                        "Deployed": true,
                        "Status": 1,
                        "ExtendPoints": 0,
                        "DeployModel": 0,
                        "CdcClusterId": "",
                        "DomainCount": 10,
                        "ClbSet": [
                            {
                                "ClbIp": "111.230.121.212"
                            },
                            {
                                "ClbIp": "192.168.1.19"
                            },
                            {
                                "ClbIp": "10.240.60.9"
                            }
                        ],
                        "Trial": 0,
                        "ModuleSet": [],
                        "UsedDomainCount": 7
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
                },
                "Account": "test102901",
                "LastChangeStatus": 1
            }
        ],
        "RequestId": "10101c75-b3ae-44fc-919c-777bfe5b2d4b",
        "TotalCount": 2
    }
}
```

