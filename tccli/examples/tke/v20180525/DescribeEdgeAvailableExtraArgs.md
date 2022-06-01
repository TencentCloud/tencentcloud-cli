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
        "ClusterVersion": "1.12.4",
        "AvailableExtraArgs": {
            "KubeControllerManager": [
                {
                    "Name": "kube-api-burst",
                    "Type": "int32",
                    "Usage": "Burst to use while talking with kubernetes apiserver. (default 30)",
                    "Default": "30"
                }
            ],
            "KubeScheduler": [],
            "Kubelet": [
                {}
            ]
        }
    },
    "RequestId": "xxx-xxxx"
}
```

