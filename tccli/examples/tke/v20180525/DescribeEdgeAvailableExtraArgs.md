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
        "ClusterVersion": "abc",
        "AvailableExtraArgs": {
            "KubeAPIServer": [
                {
                    "Name": "abc",
                    "Type": "abc",
                    "Usage": "abc",
                    "Default": "abc",
                    "Constraint": "abc"
                }
            ],
            "KubeControllerManager": [
                {
                    "Name": "abc",
                    "Type": "abc",
                    "Usage": "abc",
                    "Default": "abc",
                    "Constraint": "abc"
                }
            ],
            "KubeScheduler": [
                {
                    "Name": "abc",
                    "Type": "abc",
                    "Usage": "abc",
                    "Default": "abc",
                    "Constraint": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

