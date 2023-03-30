**Example 1: 查询集群列表**

查询集群列表。

Input: 

```
tccli thpc DescribeClusters --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ClusterSet": [
            {
                "ClusterId": "hpc-qrb7ybn0",
                "ClusterName": "unnamed",
                "ClusterStatus": "RUNNING",
                "Placement": {
                    "Zone": "ap-guangzhou-2"
                },
                "CreateTime": "2021-12-07T03:29:09Z",
                "SchedulerType": "SGE",
                "VpcId": "vpc-xxxxxxxx",
                "ComputeNodeCount": 1,
                "LoginNodeSet": [
                    {
                        "NodeId": "ins-jehc407m"
                    }
                ],
                "LoginNodeCount": 1,
                "ComputeNodeSet": [
                    {
                        "NodeId": "ins-jfhc307q"
                    }
                ],
                "ManagerNodeCount": 1,
                "ManagerNodeSet": [
                    {
                        "NodeId": "ins-cv6ygpkq"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "8a39c8e3-129b-4628-b763-ef96caaa2f4d"
    }
}
```

