**Example 1: 查询HPC集群列表**

查询HPC集群列表。

Input: 

```
tccli omics DescribeHPCClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ClusterId": "hpc-an7qz1jg",
                "CreateTime": "2024-08-07T16:00:00+08:00",
                "Description": "test hpc desc",
                "Name": "test hpc",
                "NodeCount": 3,
                "Scheduler": "SLURM",
                "Status": "RUNNING",
                "Tags": null,
                "VPCId": "vpc-36feogq7"
            }
        ],
        "RequestId": "e01bb16d-e71f-4522-ac67-51591f999dae",
        "TotalCount": 1
    }
}
```

