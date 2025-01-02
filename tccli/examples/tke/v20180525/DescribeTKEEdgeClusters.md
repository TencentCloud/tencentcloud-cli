**Example 1: 集群信息列表**

查询集群列表，用于获取集群列表

Input: 

```
tccli tke DescribeTKEEdgeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Clusters": [
            {
                "ClusterId": "test",
                "ClusterName": "test",
                "VpcId": "test",
                "PodCIDR": "test",
                "ServiceCIDR": "test",
                "K8SVersion": "test",
                "Status": "test",
                "ClusterDesc": "test",
                "CreatedTime": "test",
                "EdgeClusterVersion": "test",
                "MaxNodePodNum": 0,
                "ClusterAdvancedSettings": {
                    "ExtraArgs": {
                        "KubeAPIServer": [
                            "test"
                        ],
                        "KubeControllerManager": [
                            "test"
                        ],
                        "KubeScheduler": [
                            "test"
                        ]
                    },
                    "Runtime": "test",
                    "ProxyMode": "test"
                },
                "Level": "test",
                "AutoUpgradeClusterLevel": true,
                "ChargeType": "test",
                "EdgeVersion": "test",
                "TagSpecification": {
                    "ResourceType": "test",
                    "Tags": [
                        {
                            "Key": "test",
                            "Value": "test"
                        }
                    ]
                }
            }
        ],
        "RequestId": "d174dcb6-659b-4ab6-9533-e470a7d91e43"
    }
}
```

