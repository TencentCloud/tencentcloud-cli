**Example 1: 查询集群的Pod列表**



Input: 

```
tccli tcss DescribeUserPodList --cli-unfold-argument  \
    --ClusterId cls-ane0zamq \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "PodList": [
            {
                "PodName": "abc",
                "Status": "abc",
                "PodIP": "abc",
                "NodeLanIP": "abc",
                "WorkloadName": "abc",
                "WorkloadKind": "abc",
                "ClusterName": "abc",
                "ClusterId": "abc",
                "Namespace": "abc",
                "Region": "abc",
                "Age": "abc",
                "StartTime": "abc",
                "Restarts": 1,
                "ServiceName": "abc",
                "ServiceCount": 1,
                "ContainerName": "abc",
                "ContainerCount": 1,
                "CPU": 1,
                "Memory": 1,
                "Labels": "abc",
                "ClusterStatus": "abc",
                "WorkloadLabels": "abc",
                "ContainerId": "abc",
                "HostName": "abc",
                "HostId": "abc",
                "ClusterType": "abc",
                "NodeName": "abc",
                "NodeType": "abc",
                "ChargeCoresCnt": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

