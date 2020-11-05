**Example 1: Querying the shard information of a TencentDB instance**



Input: 

```
tccli dcdb DescribeDCDBShards --cli-unfold-argument  \
    --InstanceId dcdbt-ovulpcjf
```

Output: 
```
{
    "Response": {
        "RequestId": "09d5c691-c180-4c7f-8bcf-1ef6d1bab40c",
        "TotalCount": 2,
        "Shards": [
            {
                "ShardId": 10244,
                "InstanceId": "dcdbt-ovulpcjf",
                "ShardSerialId": "set_1536756357_1",
                "ShardInstanceId": "shard-5d4efnj7",
                "Status": 2,
                "StatusDesc": "Running",
                "CreateTime": "2018-09-12 20:44:47",
                "VpcId": "vpc-5rkcp0wb",
                "SubnetId": "subnet-6ffate6q",
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-1",
                "Memory": 2,
                "Storage": 10,
                "PeriodEndTime": "2018-10-12 20:44:47",
                "NodeCount": 2,
                "StorageUsage": 0.1,
                "MemoryUsage": 37.2
            },
            {
                "ShardId": 10245,
                "InstanceId": "dcdbt-ovulpcjf",
                "ShardSerialId": "set_1536756415_3",
                "ShardInstanceId": "shard-8huhv1y9",
                "Status": 2,
                "StatusDesc": "Running",
                "CreateTime": "2018-09-12 20:44:47",
                "VpcId": "vpc-5rkcp0wb",
                "SubnetId": "subnet-6ffate6q",
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-1",
                "Memory": 2,
                "Storage": 10,
                "PeriodEndTime": "2018-10-12 20:44:47",
                "NodeCount": 2,
                "StorageUsage": 0.1,
                "MemoryUsage": 15.1
            }
        ]
    }
}
```

