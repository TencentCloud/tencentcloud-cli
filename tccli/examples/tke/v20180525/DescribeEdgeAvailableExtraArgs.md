**Example 1: 查询集群可用的自定义参数**



Input: 

```
tccli tke DescribeEdgeAvailableExtraArgs --cli-unfold-argument  \
    --ClusterVersion 1.12.4
```

Output: 
```
{
    "Response": {
        "ClusterVersion": "test",
        "AvailableExtraArgs": {
            "KubeAPIServer": [
                {
                    "Name": "test",
                    "Type": "test",
                    "Usage": "test",
                    "Default": "test",
                    "Constraint": "test"
                }
            ],
            "KubeControllerManager": [
                {
                    "Name": "test",
                    "Type": "test",
                    "Usage": "test",
                    "Default": "test",
                    "Constraint": "test"
                }
            ],
            "KubeScheduler": [
                {
                    "Name": "test",
                    "Type": "test",
                    "Usage": "test",
                    "Default": "test",
                    "Constraint": "test"
                }
            ],
            "Kubelet": [
                {
                    "Name": "test",
                    "Type": "test",
                    "Usage": "test",
                    "Default": "test",
                    "Constraint": "test"
                }
            ]
        },
        "RequestId": "d174dcb6-659b-4ab6-9533-e470a7d91e43"
    }
}
```

