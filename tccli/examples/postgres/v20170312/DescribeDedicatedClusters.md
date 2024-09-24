**Example 1: 查询所有专属集群**

查询所有专属集群

Input: 

```
tccli postgres DescribeDedicatedClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DedicatedClusterSet": [
            {
                "CpuAvailable": 192,
                "CpuTotal": 192,
                "DedicatedClusterId": "cluster-0jend45y",
                "DiskAvailable": 1000,
                "DiskTotal": 1000,
                "InstanceCount": 0,
                "MemAvailable": 512,
                "MemTotal": 512,
                "Name": "",
                "StandbyDedicatedClusterSet": [
                    "[\"cluster-0jend45y\"",
                    "\"cluster-d8htgb6k\"]"
                ],
                "Zone": "ap-guangzhou-2"
            },
            {
                "CpuAvailable": 192,
                "CpuTotal": 192,
                "DedicatedClusterId": "cluster-d8htgb6k",
                "DiskAvailable": 1000,
                "DiskTotal": 1000,
                "InstanceCount": 0,
                "MemAvailable": 512,
                "MemTotal": 512,
                "Name": "",
                "StandbyDedicatedClusterSet": [
                    "[\"cluster-0jend45y\"",
                    "\"cluster-d8htgb6k\"]"
                ],
                "Zone": "ap-guangzhou-2"
            }
        ],
        "RequestId": "187a6206-4811-447d-b223-87a8dd470c8c"
    }
}
```

**Example 2: 查询特定专属集群**

查询专属集群cluster-0jend45y

Input: 

```
tccli postgres DescribeDedicatedClusters --cli-unfold-argument  \
    --Filters.0.Name dedicated-cluster-id \
    --Filters.0.Values cluster-0jend45y
```

Output: 
```
{
    "Response": {
        "DedicatedClusterSet": [
            {
                "CpuAvailable": 192,
                "CpuTotal": 192,
                "DedicatedClusterId": "cluster-0jend45y",
                "DiskAvailable": 1000,
                "DiskTotal": 1000,
                "InstanceCount": 0,
                "MemAvailable": 512,
                "MemTotal": 512,
                "Name": "",
                "StandbyDedicatedClusterSet": [
                    "[\"cluster-0jend45y\"",
                    "\"cluster-d8htgb6k\"]"
                ],
                "Zone": "ap-guangzhou-2"
            }
        ],
        "RequestId": "04fcd633-8e56-4c2f-9783-7c49e00647f6"
    }
}
```

