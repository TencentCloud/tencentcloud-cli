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
                "QGPUShareEnable": true,
                "EnableExternalNode": true,
                "ClusterMaterNodeNum": 1,
                "CreatedTime": "xx",
                "ClusterLevel": "xx",
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
                "ClusterNodeNum": 1,
                "ClusterDescription": "xx",
                "ImageId": "xx",
                "ContainerRuntime": "xx",
                "ClusterOs": "xx",
                "AutoUpgradeClusterLevel": true,
                "OsCustomizeType": "xx",
                "ProjectId": 1,
                "ClusterId": "xx",
                "ClusterType": "xx",
                "ClusterStatus": "xx",
                "Property": "xx",
                "DeletionProtection": true,
                "ClusterName": "xx",
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
                    "IgnoreServiceCIDRConflict": true,
                    "IgnoreClusterCIDRConflict": true,
                    "Cni": true
                }
            }
        ]
    }
}
```

