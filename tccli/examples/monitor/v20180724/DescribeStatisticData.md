**Example 1: 根据维度条件查询监控数据**

查询“K8sPodCpuCoreUsed”指标监控数据

Input: 

```
tccli monitor DescribeStatisticData --cli-unfold-argument  \
    --Module monitor \
    --Namespace QCE/TKE2 \
    --MetricNames K8sPodCpuCoreUsed \
    --Period 300 \
    --Conditions.0.Key tke_cluster_instance_id \
    --Conditions.0.Operator = \
    --Conditions.0.Value cls-mw2w40s7 \
    --StartTime 2020-11-24T15:15:50+08:00 \
    --EndTime 2020-11-24T15:25:50+08:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "MetricName": "K8sPodCpuCoreUsed",
                "Points": [
                    {
                        "Dimensions": [
                            {
                                "Name": "tke_cluster_instance_id",
                                "Value": "cls-mw2w40s7"
                            },
                            {
                                "Name": "node",
                                "Value": "cls-gn7vut9a-virtual-kubelet-subnet-node-2"
                            },
                            {
                                "Name": "pod_name",
                                "Value": "proxy-edge-j7j95"
                            },
                            {
                                "Name": "workload_name",
                                "Value": "init-test-nfs02"
                            },
                            {
                                "Name": "namespace",
                                "Value": "default-test"
                            },
                            {
                                "Name": "node_role",
                                "Value": "node"
                            },
                            {
                                "Name": "un_instance_id",
                                "Value": "cls-gn7vut9a-virtual-kubelet-subnet-nmpi5ecw-1"
                            },
                            {
                                "Name": "workload_kind",
                                "Value": "Deployment"
                            }
                        ],
                        "Values": [
                            {
                                "Timestamp": 1606202100,
                                "Value": 41.066
                            },
                            {
                                "Timestamp": 1606202400,
                                "Value": 38.666
                            },
                            {
                                "Timestamp": 1606202700,
                                "Value": 37.866
                            }
                        ]
                    },
                    {
                        "Dimensions": [
                            {
                                "Name": "namespace",
                                "Value": "default-test"
                            },
                            {
                                "Name": "node",
                                "Value": "cls-gn7vut9a-virtual-kubelet-subnet-node-3"
                            },
                            {
                                "Name": "node_role",
                                "Value": "node"
                            },
                            {
                                "Name": "pod_name",
                                "Value": "network-tools-b94d6dd89-flf7n"
                            },
                            {
                                "Name": "un_instance_id",
                                "Value": "cls-gn7vut9a-virtual-kubelet-subnet-nmpi5ecw-1"
                            },
                            {
                                "Name": "workload_kind",
                                "Value": "Deployment"
                            },
                            {
                                "Name": "workload_name",
                                "Value": "init-test-nfs00"
                            },
                            {
                                "Name": "tke_cluster_instance_id",
                                "Value": "cls-mw2w40s7"
                            }
                        ],
                        "Values": [
                            {
                                "Timestamp": 1606202100,
                                "Value": 42.666
                            },
                            {
                                "Timestamp": 1606202400,
                                "Value": 33.6
                            },
                            {
                                "Timestamp": 1606202700,
                                "Value": 40.266
                            }
                        ]
                    }
                ]
            }
        ],
        "EndTime": "2020-11-24 15:25:00",
        "Period": 300,
        "RequestId": "0d25d659-71ee-4c93-b8e1-f3992c61ff46",
        "StartTime": "2020-11-24 15:15:00"
    }
}
```

