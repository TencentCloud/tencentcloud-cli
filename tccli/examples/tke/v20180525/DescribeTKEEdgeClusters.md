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
                "ClusterId": "cls-j0hy001q",
                "ClusterName": "production-cluster",
                "VpcId": "vpc-j0hy001q",
                "PodCIDR": "10.244.0.0/16",
                "ServiceCIDR": "10.96.0.0/12",
                "K8SVersion": "1.24.4",
                "Status": "Running",
                "ClusterDesc": "Primary production Kubernetes cluster",
                "CreatedTime": "2023-10-01T12:00:00Z",
                "EdgeClusterVersion": "1.24.4",
                "MaxNodePodNum": 110,
                "ClusterAdvancedSettings": {
                    "ExtraArgs": {
                        "KubeAPIServer": [
                            "--enable-admission-plugins=NodeRestriction"
                        ],
                        "KubeControllerManager": [
                            "--node-cidr-mask-size=24"
                        ],
                        "KubeScheduler": [
                            "--scheduler-name=default-scheduler"
                        ]
                    },
                    "Runtime": "containerd",
                    "ProxyMode": "ipvs"
                },
                "Level": "L5",
                "AutoUpgradeClusterLevel": true,
                "ChargeType": "PostPaid",
                "EdgeVersion": "v1.24.3-edge",
                "TagSpecification": {
                    "ResourceType": "cluster",
                    "Tags": [
                        {
                            "Key": "Environment",
                            "Value": "Production"
                        },
                        {
                            "Key": "Owner",
                            "Value": "DevOps"
                        }
                    ]
                }
            }
        ],
        "RequestId": "d174dcb6-659b-4ab6-9533-e470a7d91e43"
    }
}
```

