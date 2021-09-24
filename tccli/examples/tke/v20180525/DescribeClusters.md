**Example 1: 查询集群列表**



Input: 

```
tccli tke DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Clusters": [
            {
                "DeletionProtection": true,
                "ClusterVersion": "xx",
                "TagSpecification": [
                    {
                        "ResourceType": "xx",
                        "Tags": [
                            {
                                "Value": "xx",
                                "Key": "xx"
                            }
                        ]
                    }
                ],
                "ClusterName": "xx",
                "ClusterId": "xx",
                "ClusterNodeNum": 1,
                "ClusterType": "xx",
                "ClusterDescription": "xx",
                "ImageId": "xx",
                "CreatedTime": "xx",
                "EnableExternalNode": true,
                "ContainerRuntime": "xx",
                "ClusterMaterNodeNum": 1,
                "ProjectId": 1,
                "OsCustomizeType": "xx",
                "ClusterNetworkSettings": {
                    "Subnets": [
                        "xx"
                    ],
                    "VpcId": "xx",
                    "ServiceCIDR": "xx",
                    "MaxClusterServiceNum": 1,
                    "KubeProxyMode": "xx",
                    "MaxNodePodNum": 1,
                    "Ipvs": true,
                    "ClusterCIDR": "xx",
                    "IgnoreClusterCIDRConflict": true,
                    "Cni": true
                },
                "Property": "xx",
                "ClusterOs": "xx",
                "ClusterStatus": "xx"
            }
        ]
    }
}
```

