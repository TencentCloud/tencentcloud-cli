**Example 1: 查看组件状态**

查看组件状态

Input: 

```
tccli camp DescribeComponentStatus --cli-unfold-argument  \
    --ProjectID prj-27np9q4t \
    --ApplicationID app-wchnr4pv \
    --InstanceID ins-xxxx \
    --ComponentName tt \
    --EnvironmentName test
```

Output: 
```
{
    "Response": {
        "ComponentStatus": {
            "Name": "dsdasdasdasd",
            "Phase": "Running",
            "CurrentRevision": "dsdasdasdasd-784449fd45",
            "UpdateRevision": "dsdasdasdasd-784449fd45",
            "ScheduleDesiredReplicas": 2,
            "DesiredReplicas": 2,
            "TotalReplicas": 2,
            "ReadyReplicas": 2,
            "UpdateRevisionReplicas": 2,
            "WorkLoads": [
                {
                    "Name": "dsdasdasdasd",
                    "APIVersion": "apps/v1",
                    "Kind": "Deployment",
                    "ScheduleDesiredReplicas": 2,
                    "DesiredReplicas": 2,
                    "TotalReplicas": 2,
                    "ReadyReplicas": 2,
                    "UpdateRevisionReplicas": 2,
                    "UpdateReadyReplicas": 2,
                    "Zones": [
                        {
                            "Zone": "ap-guangzhou-4",
                            "Region": "ap-guangzhou",
                            "PlacementName": "gz",
                            "ScheduleDesiredReplicas": 1,
                            "DesiredReplicas": 1,
                            "TotalReplicas": 1,
                            "ReadyReplicas": 1,
                            "UpdateRevisionReplicas": 1,
                            "UpdateReadyReplicas": 1
                        }
                    ],
                    "Clusters": [
                        {
                            "ClusterID": "cls-fsiq95a4",
                            "ScheduleDesiredReplicas": 1,
                            "DesiredReplicas": 1,
                            "TotalReplicas": 1,
                            "ReadyReplicas": 1,
                            "UpdateRevisionReplicas": 1,
                            "UpdateReadyReplicas": 1
                        }
                    ]
                }
            ],
            "PlacementTopologyReplicas": [],
            "Traits": [
                {
                    "Name": "",
                    "Type": "replicas",
                    "Complete": true
                },
                {
                    "Name": "",
                    "Type": "network-qos",
                    "Complete": true
                }
            ],
            "Message": ""
        },
        "PodStatus": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-4",
                "Running": 1,
                "Succeeded": 0,
                "Failed": 0,
                "Pending": 0
            },
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "Running": 1,
                "Succeeded": 0,
                "Failed": 0,
                "Pending": 0
            }
        ],
        "RequestId": "389e4af0-f077-4466-a74d-14a0bdeeff73"
    }
}
```

