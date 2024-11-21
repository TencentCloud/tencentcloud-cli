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
                "Age": "303h45m31.069895614s",
                "CPU": 0,
                "ChargeCoresCnt": 0,
                "ClusterId": "cls-abhq0j4o",
                "ClusterName": "bx_test_tmp",
                "ClusterStatus": "CSR_RUNNING",
                "ClusterType": "INDEPENDENT_CLUSTER",
                "ContainerCount": 0,
                "ContainerId": "",
                "ContainerName": "",
                "HostId": "ins-qj24hgj0",
                "HostName": "",
                "Labels": "",
                "Memory": 0,
                "Namespace": "default",
                "NodeLanIP": "10.0.0.14",
                "NodeName": "",
                "NodeType": "NORMAL",
                "PodIP": "192.168.0.172",
                "PodName": "tiefighter",
                "Region": "ap-guangzhou",
                "Restarts": 0,
                "ServiceCount": 0,
                "ServiceName": "",
                "StartTime": "2024-10-17 23:03:42",
                "Status": "Running",
                "WorkloadKind": "",
                "WorkloadLabels": "",
                "WorkloadName": ""
            }
        ],
        "RequestId": "1d32a744-4f31-4a6b-8574-7919f034f317",
        "TotalCount": 54
    }
}
```

