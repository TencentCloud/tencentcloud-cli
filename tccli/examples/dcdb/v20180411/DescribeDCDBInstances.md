**Example 1: 根据实例ID查询实例列表**



Input: 

```
tccli dcdb DescribeDCDBInstances --cli-unfold-argument  \
    --InstanceIds tdsqlshard-hptutl5t
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AppId": 251000022,
                "AutoRenewFlag": 1,
                "Cpu": 2,
                "CreateTime": "2021-03-26 16:14:31",
                "DbEngine": "MariaDB",
                "DbVersion": "10.1.9",
                "DcnDstNum": 0,
                "DcnFlag": 0,
                "DcnStatus": 0,
                "ExclusterId": "",
                "Id": 2000091,
                "InstanceId": "tdsqlshard-hptutl5t",
                "InstanceName": "tdsqlshard-hptutl5t",
                "InstanceType": 2,
                "Ipv6Flag": 0,
                "IsAuditSupported": 1,
                "IsTmp": 0,
                "IsolatedTimestamp": "0000-00-00 00:00:00",
                "Locker": 0,
                "Memory": 4,
                "NodeCount": 2,
                "Paymode": "prepaid",
                "PeriodEndTime": "2021-04-26 16:14:31",
                "Pid": 1001670,
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "ShardCount": 2,
                "ShardDetail": [
                    {
                        "Cpu": 1,
                        "Createtime": "2021-03-26 16:14:31",
                        "Memory": 2,
                        "NodeCount": 1,
                        "Pid": 1001670,
                        "ShardId": 12208,
                        "ShardInstanceId": "shard-qihco4rx",
                        "ShardSerialId": "set_1616746585_1",
                        "Status": 2,
                        "Storage": 10
                    },
                    {
                        "Cpu": 1,
                        "Createtime": "2021-03-26 16:14:31",
                        "Memory": 2,
                        "NodeCount": 1,
                        "Pid": 1001670,
                        "ShardId": 12209,
                        "ShardInstanceId": "shard-d3moxo2r",
                        "ShardSerialId": "set_1616746676_3",
                        "Status": 2,
                        "Storage": 10
                    }
                ],
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 20,
                "SubnetId": 1479311,
                "Uin": "918700682",
                "UniqueSubnetId": "subnet-au6ics6s",
                "UniqueVpcId": "vpc-737mtr2f",
                "UpdateTime": "2021-03-29 15:35:33",
                "Vip": "10.1.0.6",
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
        "RequestId": "a44a3d24-1e71-4bbf-bc22-f6d583b084d8",
        "TotalCount": 1
    }
}
```

