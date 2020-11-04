**Example 1: 根据实例ID查询实例列表**



Input: 

```
tccli dcdb DescribeDCDBInstances --cli-unfold-argument  \
    --InstanceIds dcdbt-52s53yyh
```

Output: 
```
{
    "Response": {
        "RequestId": "f5301a70-8a4b-4e5e-b7e4-68d9c2f9c7c6",
        "TotalCount": 1,
        "Instances": [
            {
                "Id": 40965,
                "InstanceId": "dcdbt-52s53yyh",
                "InstanceName": "dcdbt-52s53yyh",
                "AppId": 1251006373,
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-2",
                "VpcId": 75203,
                "SubnetId": 45109,
                "UniqueVpcId": "vpc-5rkcp0wb",
                "UniqueSubnetId": "subnet-6ffate6q",
                "Status": 2,
                "StatusDesc": "运行中",
                "Vip": "172.17.0.10",
                "Vport": 3306,
                "WanDomain": "",
                "WanVip": "",
                "WanPort": 0,
                "CreateTime": "2018-05-04 16:42:18",
                "UpdateTime": "2018-05-20 18:04:17",
                "AutoRenewFlag": 0,
                "NodeCount": 2,
                "IsTmp": 0,
                "ExclusterId": "",
                "Memory": 4,
                "Storage": 20,
                "ShardCount": 2,
                "PeriodEndTime": "2018-05-11 16:42:18",
                "IsolatedTimestamp": "0000-00-00 00:00:00",
                "DbVersion": "10.1.9",
                "DbEngine": "MySQL",
                "Uin": "20548499",
                "Pid": 11128,
                "ShardDetail": [
                    {
                        "ShardId": 10240,
                        "ShardInstanceId": "shard-8m3rgssh",
                        "ShardSerialId": "set_1525423498_1",
                        "Status": 2,
                        "Createtime": "2018-05-04 16:42:19",
                        "Memory": 2,
                        "Storage": 10,
                        "Pid": 11128,
                        "NodeCount": 2
                    },
                    {
                        "ShardId": 10241,
                        "ShardInstanceId": "shard-n8f80yrv",
                        "ShardSerialId": "set_1525427618_3",
                        "Status": 2,
                        "Createtime": "2018-05-04 16:42:19",
                        "Memory": 2,
                        "Storage": 10,
                        "Pid": 11128,
                        "NodeCount": 2
                    }
                ]
            }
        ]
    }
}
```

