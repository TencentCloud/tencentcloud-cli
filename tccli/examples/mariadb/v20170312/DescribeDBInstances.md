**Example 1: 根据实例ID查询实例列表**



Input: 

```
tccli mariadb DescribeDBInstances --cli-unfold-argument  \
    --InstanceIds tdsql-dj77jd0p
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AppId": 251000022,
                "AutoRenewFlag": 1,
                "Cpu": 1,
                "CreateTime": "2021-03-26 15:28:23",
                "DbEngine": "Percona",
                "DbVersion": "5.7.17",
                "DcnDstNum": 0,
                "DcnFlag": 0,
                "DcnStatus": 0,
                "ExclusterId": "",
                "Id": 2000090,
                "InstanceId": "tdsql-dj77jd0p",
                "InstanceName": "tdsql-dj77jd0p",
                "InstanceType": 2,
                "Ipv6Flag": 0,
                "IsAuditSupported": 1,
                "IsEncryptSupported": 1,
                "IsTmp": 0,
                "Locker": 0,
                "Machine": "TS85",
                "Memory": 2,
                "NodeCount": 2,
                "OriginSerialId": "set_1616743781_36017514",
                "Paymode": "prepaid",
                "PeriodEndTime": "2021-04-26 15:28:23",
                "Pid": 1002231,
                "ProjectId": 0,
                "Qps": 2100,
                "Region": "ap-guangzhou",
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "SubnetId": 1479311,
                "TdsqlVersion": "基于Percona 5.7.17设计(兼容Mysql 5.7)",
                "Uin": "918700682",
                "UniqueSubnetId": "subnet-au6ics6s",
                "UniqueVpcId": "vpc-737mtr2f",
                "UpdateTime": "2021-03-29 17:20:05",
                "Vip": "10.1.0.10",
                "Vipv6": "",
                "VpcId": 74809,
                "Vport": 3306,
                "WanDomain": "",
                "WanPort": 0,
                "WanPortIpv6": 0,
                "WanStatus": 0,
                "WanStatusIpv6": 0,
                "WanVip": "",
                "WanVipv6": "",
                "Zone": "ap-guangzhou-1",
                "ResourceTags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ]
            }
        ],
        "RequestId": "66c4d0c5-bdef-45bd-aa5b-05642802d034",
        "TotalCount": 1
    }
}
```

