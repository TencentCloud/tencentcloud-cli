**Example 1: 查询改密计划详情**

查询改密计划详情

Input: 

```
tccli dasb DescribeChangePwdTaskDetail --cli-unfold-argument  \
    --OperationId ops-addsfa \
    --Filters.0.Name InstanceId \
    --Filters.0.Values ins-asdfasdffas \
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
                    "InstanceId": "ins-bhtest",
                    "Name": "linux",
                    "PublicIp": "100.10.1.1",
                    "PrivateIp": "172.20.0.1",
                    "ApCode": "ap-shanghai-fsi",
                    "OsName": "TencentOS Server 3.1 (TK4)",
                    "Kind": 1,
                    "Port": 22,
                    "IpPortSet": [
                        "127.0.0.1:80"
                    ],
                    "VpcId": "vpc-bhtest",
                    "SubnetId": "subnet-bhtest",
                    "AccountCount": 0,
                    "GroupSet": [
                        {
                            "Id": 1,
                            "Name": "测试组",
                            "Department": {
                                "Id": "1.2",
                                "Name": "运维部",
                                "Managers": [],
                                "ManagerUsers": []
                            },
                            "Count": 1
                        }
                    ],
                    "Resource": {
                        "ResourceId": "bh-saas-test",
                        "ResourceName": "T-Sec-堡垒机（SaaS型）/专业版",
                        "ApCode": "ap-shanghai-fsi",
                        "Zone": "ap-shanghai-fsi-1",
                        "Pid": 10,
                        "SvArgs": "sv_cds_dasb_saas_ex_pro_sdfsa",
                        "PackageBandwidth": 0,
                        "PackageNode": 0,
                        "LogDeliveryArgs": "sv_cds_dasb_saas_sadsas",
                        "LogDelivery": "sc_cds_dasb_saas_asawda",
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
                        "DeployModel": 0,
                        "CdcClusterId": "cdc-dfsed-eda",
                        "ModuleSet": []
                    },
                    "Department": {
                        "Id": "1",
                        "Name": "总部",
                        "Managers": [],
                        "ManagerUsers": []
                    }
                },
                "Account": "worktest",
                "LastChangeStatus": 1
            }
        ],
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af",
        "TotalCount": 1
    }
}
```

