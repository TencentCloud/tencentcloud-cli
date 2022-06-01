**Example 1: 查询集群自定义参数**



Input: 

```
tccli tke DescribeEdgeClusterExtraArgs --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "ClusterExtraArgs": {
            "KubeAPIServer": [
                "max-mutating-requests-inflight=500"
            ],
            "KubeControllerManager": [
                "kube-api-burst=500"
            ],
            "KubeScheduler": [
                "kube-api-burst=500"
            ]
        },
        "RequestId": "5a489220-1730-43ee-9a59-7d3a752ac750"
    }
}
```

