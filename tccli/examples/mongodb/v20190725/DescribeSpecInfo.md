**Example 1: 查询云数据库售卖**



Input: 

```
tccli mongodb DescribeSpecInfo --cli-unfold-argument  \
    --Zone xx
```

Output: 
```
{
    "Response": {
        "RequestId": "a8c7ade4-2d22-4f5e-9e71-f546f15e6d67",
        "SpecInfoList": [
            {
                "Region": "ap-guangzhou",
                "SpecItems": [
                    {
                        "ClusterType": 0,
                        "Conns": 1500,
                        "Cpu": 2,
                        "DefaultStorage": 25600,
                        "EngineName": "WiredTiger",
                        "MachineType": "HIO10G",
                        "MaxNodeNum": 3,
                        "MaxReplicateSetNodeNum": 5,
                        "MaxReplicateSetNum": 20,
                        "MaxStorage": 512000,
                        "Memory": 4096,
                        "MinNodeNum": 3,
                        "MinReplicateSetNodeNum": 3,
                        "MinReplicateSetNum": 2,
                        "MinStorage": 102400,
                        "MongoVersionCode": "MONGO_36_WT",
                        "MongoVersionValue": 4,
                        "Qps": 5000,
                        "SpecCode": "mongo.HIO10G.4g",
                        "Status": 1,
                        "Version": "3.6"
                    },
                    {
                        "ClusterType": 0,
                        "Conns": 1500,
                        "Cpu": 2,
                        "DefaultStorage": 25600,
                        "EngineName": "WiredTiger",
                        "MachineType": "HIO10G",
                        "MaxNodeNum": 3,
                        "MaxReplicateSetNodeNum": 5,
                        "MaxReplicateSetNum": 20,
                        "MaxStorage": 512000,
                        "Memory": 4096,
                        "MinNodeNum": 3,
                        "MinReplicateSetNodeNum": 3,
                        "MinReplicateSetNum": 2,
                        "MinStorage": 102400,
                        "MongoVersionCode": "MONGO_3_WT",
                        "MongoVersionValue": 2,
                        "Qps": 5000,
                        "SpecCode": "mongo.HIO10G.4g",
                        "Status": 1,
                        "Version": "3.2"
                    },
                    {
                        "ClusterType": 1,
                        "Conns": 15000,
                        "Cpu": 48,
                        "DefaultStorage": 4096000,
                        "EngineName": "WiredTiger",
                        "MachineType": "HIO10G",
                        "MaxNodeNum": 3,
                        "MaxReplicateSetNodeNum": 5,
                        "MaxReplicateSetNum": 20,
                        "MaxStorage": 6144000,
                        "Memory": 524288,
                        "MinNodeNum": 3,
                        "MinReplicateSetNodeNum": 3,
                        "MinReplicateSetNum": 2,
                        "MinStorage": 1536000,
                        "MongoVersionCode": "MONGO_36_WT",
                        "MongoVersionValue": 4,
                        "Qps": 42000,
                        "SpecCode": "mongo.HIO10G.512g",
                        "Status": 1,
                        "Version": "3.6"
                    }
                ],
                "Zone": "ap-guangzhou-3"
            }
        ]
    }
}
```

