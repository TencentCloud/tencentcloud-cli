**Example 1: 查询 TKE 节点池列表**

查询 TKE 节点池列表

Input: 

```
tccli tke DescribeNodePools --cli-unfold-argument  \
    --ClusterId cls-h8atd7dj \
    --Filters.0.Name NodePoolsName \
    --Filters.0.Values cputest \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "NodePools": [
            {
                "Annotations": [],
                "ClusterId": "cls-h8atd7dj",
                "CreatedAt": "2023-01-15 17:55:38 +0000 UTC",
                "DeletionProtection": false,
                "External": null,
                "Labels": [],
                "LifeState": "normal",
                "Name": "cputest",
                "Native": null,
                "NodePoolId": "np-rbl9quwv",
                "Regular": {
                    "AutoscalingGroupId": "asg-mv6aoc57",
                    "AutoscalingGroupStatus": "disabled",
                    "DesiredNodesNum": 0,
                    "InstanceAdvancedSettings": {
                        "DesiredPodNumber": 32,
                        "ExtraArgs": {
                            "Kubelet": null
                        },
                        "PreStartUserScript": "",
                        "RuntimeConfig": {
                            "RuntimeRootDir": "",
                            "RuntimeType": "docker",
                            "RuntimeVersion": "19.3"
                        },
                        "UserScript": ""
                    },
                    "LaunchConfigurationId": "asc-ay1hkbqh",
                    "MaxNodesNum": 1,
                    "MinNodesNum": 0,
                    "NodeCountSummary": {
                        "AutoscalingAdded": {
                            "Initializing": 0,
                            "Joining": 0,
                            "Normal": 0,
                            "Total": 0
                        },
                        "ManuallyAdded": {
                            "Initializing": 0,
                            "Joining": 0,
                            "Normal": 0,
                            "Total": 0
                        }
                    },
                    "NodePoolOs": "ubuntu20.04x86_64"
                },
                "Super": null,
                "Tags": [],
                "Taints": [],
                "Type": "Regular",
                "Unschedulable": false
            },
            {
                "Annotations": [],
                "ClusterId": "cls-h8att7dj",
                "CreatedAt": "2023-11-16 20:56:55 +0000 UTC",
                "DeletionProtection": true,
                "External": {
                    "NodesNum": 1,
                    "RuntimeConfig": {
                        "RuntimeRootDir": null,
                        "RuntimeType": "docker",
                        "RuntimeVersion": "docker-19.3"
                    }
                },
                "Labels": [
                    {
                        "Name": "node.kubernetes.io/instance-type",
                        "Value": "external"
                    },
                    {
                        "Name": "tke.cloud.tencent.com/cbs-mountable",
                        "Value": "false"
                    },
                    {
                        "Name": "externalnode.tke.cloud.tencent.com/version",
                        "Value": "v2"
                    }
                ],
                "LifeState": "Running",
                "Name": "cpu",
                "Native": null,
                "NodePoolId": "np-llfflb19",
                "Regular": null,
                "Super": null,
                "Tags": [],
                "Taints": [],
                "Type": "External",
                "Unschedulable": false
            },
            {
                "Annotations": [],
                "ClusterId": "cls-h8att7dj",
                "CreatedAt": "2023-11-16 20:56:54 +0000 UTC",
                "DeletionProtection": true,
                "External": {
                    "NodesNum": 4,
                    "RuntimeConfig": {
                        "RuntimeRootDir": null,
                        "RuntimeType": "docker",
                        "RuntimeVersion": "docker-19.3"
                    }
                },
                "Labels": [
                    {
                        "Name": "externalnode.tke.cloud.tencent.com/version",
                        "Value": "v2"
                    },
                    {
                        "Name": "node.kubernetes.io/instance-type",
                        "Value": "external"
                    },
                    {
                        "Name": "nvidia-device-enable",
                        "Value": "enable"
                    },
                    {
                        "Name": "tke.cloud.tencent.com/cbs-mountable",
                        "Value": "false"
                    }
                ],
                "LifeState": "Running",
                "Name": "gpu",
                "Native": null,
                "NodePoolId": "np-iw0qds8t",
                "Regular": null,
                "Super": null,
                "Tags": [],
                "Taints": [],
                "Type": "External",
                "Unschedulable": false
            }
        ],
        "RequestId": "354c45c4-0eb2-464d-82f8-3dd55ca88a80",
        "TotalCount": 3
    }
}
```

