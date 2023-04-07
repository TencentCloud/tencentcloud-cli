**Example 1: 查询集群列表**



Input: 

```
tccli tke DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "AutoUpgradeClusterLevel": true,
                "ClusterDescription": "",
                "ClusterEtcdNodeNum": 0,
                "ClusterId": "cls-ayzfpv5c",
                "ClusterLevel": "L5",
                "ClusterMaterNodeNum": 1,
                "ClusterName": "yctest",
                "ClusterNetworkSettings": {
                    "CiliumMode": "",
                    "ClusterCIDR": "10.12.0.0/14",
                    "Cni": true,
                    "IgnoreClusterCIDRConflict": false,
                    "IgnoreServiceCIDRConflict": false,
                    "Ipv6ServiceCIDR": "",
                    "Ipvs": false,
                    "IsDualStack": false,
                    "KubeProxyMode": "",
                    "MaxClusterServiceNum": 1024,
                    "MaxNodePodNum": 64,
                    "ServiceCIDR": "10.15.252.0/22",
                    "Subnets": null,
                    "VpcId": "vpc-7modfjc3"
                },
                "ClusterNodeNum": 2,
                "ClusterOs": "tlinux3.1x86_64",
                "ClusterStatus": "Running",
                "ClusterType": "MANAGED_CLUSTER",
                "ClusterVersion": "1.24.4",
                "ContainerRuntime": "containerd",
                "CreatedTime": "2022-12-27T07:46:13Z",
                "DeletionProtection": true,
                "EnableExternalNode": false,
                "ImageId": "",
                "OsCustomizeType": "GENERAL",
                "ProjectId": 0,
                "Property": "{\"NodeNameType\":\"lan-ip\",\"NetworkType\":\"GR\"}",
                "QGPUShareEnable": false,
                "RuntimeVersion": "1.4.3",
                "TagSpecification": null
            }
        ],
        "RequestId": "583e6c4b-ff24-42f8-87f1-37e4c00d81b7",
        "TotalCount": 1
    }
}
```

