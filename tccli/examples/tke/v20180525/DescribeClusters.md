**Example 1: 查询集群列表**

查询集群列表，用于获取集群列表

Input: 

```
tccli tke DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Clusters": [
            {
                "ClusterId": "cls-xxxxxxx",
                "ClusterName": "集群",
                "ClusterDescription": "",
                "ClusterVersion": "1.10.5",
                "ClusterOs": "ubuntu16.04.1 LTSx86_64",
                "ClusterType": "INDEPENDENT_CLUSTER",
                "ClusterNetworkSettings": {
                    "ClusterCIDR": "10.211.0.0/16",
                    "IgnoreClusterCIDRConflict": false,
                    "MaxNodePodNum": 256,
                    "MaxClusterServiceNum": 256,
                    "Ipvs": false,
                    "VpcId": "vpc-xxxxxx"
                },
                "ClusterNodeNum": 3
            }
        ],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

