**Example 1: 无**



Input: 

```
tccli dcdb DescribeDCDBShards --cli-unfold-argument  \
    --InstanceId dcdbt-21dfpcv1
```

Output: 
```
{
    "Response": {
        "DcnFlag": 0,
        "RequestId": "f976f43c-6dd3-4dbf-869b-a1b0eac50506",
        "Shards": [
            {
                "Cpu": 2,
                "CreateTime": "2021-12-01 11:49:54",
                "InstanceId": "dcdbt-21dfpcv1",
                "Memory": 4,
                "MemoryUsage": 0.94,
                "NodeCount": 2,
                "Paymode": "prepaid",
                "PeriodEndTime": "2023-01-01 11:12:24",
                "Pid": 1002231,
                "ProjectId": 0,
                "ProxyVersion": "\"1.17.6-M-V2.0R723D002\"",
                "Range": "0-31",
                "Region": "ap-guangzhou",
                "ShardId": 434,
                "ShardInstanceId": "shard-ngbrea6b",
                "ShardMasterZone": "ap-guangzhou-1",
                "ShardSerialId": "set_1643096858_1",
                "ShardSlaveZones": [
                    "ap-guangzhou-1"
                ],
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "StorageUsage": 0.01,
                "SubnetId": "subnet-ovkcc9x6",
                "VpcId": "vpc-j97vcvb5",
                "Zone": "ap-guangzhou-2"
            },
            {
                "Cpu": 1,
                "CreateTime": "2021-12-01 11:49:54",
                "InstanceId": "dcdbt-21dfpcv1",
                "Memory": 2,
                "MemoryUsage": 0.99,
                "NodeCount": 2,
                "Paymode": "prepaid",
                "PeriodEndTime": "2023-01-01 11:12:24",
                "Pid": 1002231,
                "ProjectId": 0,
                "ProxyVersion": "\"1.17.6-M-V2.0R723D002\"",
                "Range": "32-63",
                "Region": "ap-guangzhou",
                "ShardId": 435,
                "ShardInstanceId": "shard-5zf65smf",
                "ShardMasterZone": "ap-guangzhou-1",
                "ShardSerialId": "set_1643096949_3",
                "ShardSlaveZones": [
                    "ap-guangzhou-1"
                ],
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "StorageUsage": 0.011,
                "SubnetId": "subnet-ovkcc9x6",
                "VpcId": "vpc-j97vcvb5",
                "Zone": "ap-guangzhou-2"
            }
        ],
        "TotalCount": 2
    }
}
```

