**Example 1: 查询云数据库售卖**



Input: 

```
tccli mongodb DescribeSpecInfo --cli-unfold-argument  \
    --Region ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "7e143607-fc69-4761-b0ba-529cb1786ef3",
        "SpecInfoList": [
            {
                "Region": "ap-guangzhou",
                "SpecItems": [
                    {
                        "ClusterType": 1,
                        "Conns": 0,
                        "Cpu": 1,
                        "DefaultStorage": 20480,
                        "EngineName": "WiredTiger",
                        "MachineType": "CONFIG_SERVER",
                        "MaxNodeNum": 32,
                        "MaxReplicateSetNodeNum": 0,
                        "MaxReplicateSetNum": 0,
                        "MaxStorage": 20480,
                        "Memory": 2048,
                        "MinNodeNum": 3,
                        "MinReplicateSetNodeNum": 0,
                        "MinReplicateSetNum": 0,
                        "MinStorage": 20480,
                        "MongoVersionCode": "MONGO_42_WT",
                        "MongoVersionValue": 9,
                        "Qps": 0,
                        "SpecCode": "cfgsrv.STD.1C2G",
                        "Status": 1,
                        "Version": "4.2"
                    }
                ],
                "Zone": "ap-guangzhou-3"
            }
        ]
    }
}
```

