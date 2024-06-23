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
                "ClusterId": "abc",
                "ClusterName": "abc",
                "VpcId": "abc",
                "PodCIDR": "abc",
                "ServiceCIDR": "abc",
                "K8SVersion": "abc",
                "Status": "abc",
                "ClusterDesc": "abc",
                "CreatedTime": "abc",
                "EdgeClusterVersion": "abc",
                "MaxNodePodNum": 0,
                "ClusterAdvancedSettings": {
                    "ExtraArgs": {
                        "KubeAPIServer": [
                            "abc"
                        ],
                        "KubeControllerManager": [
                            "abc"
                        ],
                        "KubeScheduler": [
                            "abc"
                        ]
                    },
                    "Runtime": "abc",
                    "ProxyMode": "abc"
                },
                "Level": "abc",
                "AutoUpgradeClusterLevel": true,
                "ChargeType": "abc",
                "EdgeVersion": "abc",
                "TagSpecification": {
                    "ResourceType": "abc",
                    "Tags": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ]
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

