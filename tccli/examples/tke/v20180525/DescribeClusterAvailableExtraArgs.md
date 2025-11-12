**Example 1: 查询集群可用的自定义参数**



Input: 

```
tccli tke DescribeClusterAvailableExtraArgs --cli-unfold-argument  \
    --ClusterVersion 1.20.6 \
    --ClusterType MANAGED_CLUSTER
```

Output: 
```
{
    "Response": {
        "ClusterVersion": "1.20.6",
        "ClusterType": "MANAGED_CLUSTER",
        "AvailableExtraArgs": {
            "KubeAPIServer": [
                {
                    "Name": "max-mutating-requests-inflight",
                    "Type": "int",
                    "Usage": "The maximum number of mutating requests in flight at a given time. When the server exceeds this, it rejects requests. Zero for no limit. (default 200)",
                    "Default": "200"
                }
            ],
            "KubeControllerManager": [
                {
                    "Name": "kube-api-burst",
                    "Type": "int32",
                    "Usage": "Burst to use while talking with kubernetes apiserver. (default 30)",
                    "Default": "30"
                }
            ],
            "KubeScheduler": [],
            "Kubelet": []
        },
        "RequestId": "74f06cc7-145d-4a3c-91ec-318561dd4b4d"
    }
}
```

