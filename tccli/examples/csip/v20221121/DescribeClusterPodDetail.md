**Example 1: 1**



Input: 

```
tccli csip DescribeClusterPodDetail --cli-unfold-argument  \
    --UniqueID 474eda3f2befc4e3072c67adf9086ce1
```

Output: 
```
{
    "Response": {
        "AlarmEventCriticalCount": 0,
        "AlarmEventHighCount": 0,
        "AlarmEventLowCount": 0,
        "AlarmEventMiddleCount": 0,
        "AppID": 260083796,
        "ClusterID": "cls-pde9e0s0",
        "ClusterName": "yancyw-标准集群",
        "ClusterRunStatus": "Running",
        "ClusterType": "TKE_MANAGED_CLUSTER",
        "ContainerCount": 1,
        "Labels": [
            {
                "TagKey": "app",
                "TagValue": "openclaw-latest"
            }
        ],
        "Namespace": "openclaw",
        "NodeExternalIP": "",
        "NodeId": "ins-08eaqwmk",
        "NodeInternalIP": "172.16.1.36",
        "NodeName": "tke_cls-pde9e0s0_worker",
        "PodIP": "172.16.0.160",
        "PodName": "openclaw-latest-7ddc9cbdb7-22vnh",
        "Region": "ap-guangzhou",
        "RestartCount": 0,
        "RiskEventCriticalCount": 0,
        "RiskEventHighCount": 0,
        "RiskEventLowCount": 0,
        "RiskEventMiddleCount": 0,
        "RunStatus": "Running",
        "ServiceCount": 1,
        "StartTime": "2026-06-12T01:56:15Z",
        "StartupTime": 2073768,
        "UniqueID": "474eda3f2befc4e3072c67adf9086ce1",
        "WorkloadName": "openclaw-latest-7ddc9cbdb7",
        "WorkloadType": "ReplicaSet",
        "RequestId": "b426ae55-fdb0-4e29-82ae-d1259b12ca72"
    }
}
```

