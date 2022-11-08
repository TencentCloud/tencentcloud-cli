**Example 1: 查询边缘集群升级信息**



Input: 

```
tccli tke DescribeEdgeClusterUpgradeInfo --cli-unfold-argument  \
    --EdgeVersion 1.0.2 \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "67a0dd10-ef28-49a1-8834-7a5fa7a9bac0",
        "EdgeVersionCurrent": "1.1.0",
        "ComponentVersion": "{\"hyperkube\":{},\"kube-proxy\":{},\"coredns\":{\"InitImageName\":\"\",\"InitImageVersion\":\"\",\"ImageName\":\"\",\"ImageVersion\":\"1.6.7\"},\"flannel\":{\"InitImageName\":\"\",\"InitImageVersion\":\"\",\"ImageName\":\"\",\"ImageVersion\":\"v0.12.0-edge-2.0\"},\"gpu-plugin\":{\"ImageName\":\"\",\"ImageVersion\":\"v0.9.0\"},\"site-manager\":{\"ImageName\":\"\",\"ImageVersion\":\"v0.6.0\"},\"application-grid-controller\":{\"ImageName\":\"\",\"ImageVersion\":\"1.21.1\"},\"application-grid-wrapper\":{\"ImageName\":\"\",\"ImageVersion\":\"1.20.3\"},\"tunnel\":{\"ImageName\":\"\",\"ImageVersion\":\"v0.8.0\"},\"edge-health\":{\"ImageName\":\"\",\"ImageVersion\":\"\"},\"edge-health-admission\":{\"ImageName\":\"\",\"ImageVersion\":\"\"},\"event\":{\"ImageName\":\"\",\"ImageVersion\":\"\"},\"griddaemon\":{\"ImageName\":\"\",\"ImageVersion\":\"\"},\"metric-server\":{\"ImageName\":\"\",\"ImageVersion\":\"\"},\"standalone-metrics\":{\"ImageName\":\"\",\"ImageVersion\":\"\"},\"hpa-metrics-server\":{\"ImageName\":\"\",\"ImageVersion\":\"\"},\"tke-monitor-agent\":{\"ImageName\":\"\",\"ImageVersion\":\"20220714-3b31e8d2\"}}",
        "RegistryPrefix": "",
        "ClusterUpgradeStatus": "updating",
        "ClusterUpgradeStatusReason": "component application-grid-controller:Back-off pulling image \"ccr.ccs.tencentyun.com/tkeedge/application-grid-controller:1.21.1-x\""
    }
}
```

