**Example 1: 查询节点池列表**

查询节点池列表

Input: 

```
tccli tke DescribeClusterNodePools --cli-unfold-argument  \
    --ClusterId cls-e55paxnt
```

Output: 
```
{
    "Response": {
        "NodePoolSet": [
            {
                "AutoscalingGroupId": "asg-e55paxnt",
                "AutoscalingGroupStatus": "disabled",
                "ClusterInstanceId": "cls-e55paxnt",
                "DataDisks": null,
                "DeletionProtection": true,
                "DesiredNodesNum": 2,
                "DesiredPodNum": 64,
                "DockerGraphPath": "",
                "ExtraArgs": {
                    "Kubelet": []
                },
                "GPUArgs": {
                    "CUDA": {
                        "Name": "",
                        "Version": ""
                    },
                    "CUDNN": {
                        "DevName": "",
                        "DocName": "",
                        "Name": "",
                        "Version": ""
                    },
                    "CustomDriver": {
                        "Address": ""
                    },
                    "Driver": {
                        "Name": "",
                        "Version": ""
                    },
                    "MIGEnable": false
                },
                "ImageId": "",
                "Labels": [],
                "Annotations": [],
                "LaunchConfigurationId": "asc-e55paxnt",
                "LifeState": "normal",
                "MaxNodesNum": 3,
                "MinNodesNum": 0,
                "Name": "未命名",
                "NodeCountSummary": {
                    "AutoscalingAdded": {
                        "Initializing": 0,
                        "Joining": 0,
                        "Normal": 2,
                        "Total": 2
                    },
                    "ManuallyAdded": {
                        "Initializing": 0,
                        "Joining": 0,
                        "Normal": 1,
                        "Total": 1
                    }
                },
                "NodePoolId": "np-e55paxnt",
                "NodePoolOs": "tlinux2.4x86_64",
                "OsCustomizeType": "GENERAL",
                "PreStartUserScript": "#!/bin/sh\ntouch /tmp/before",
                "RuntimeConfig": {
                    "RuntimeType": "containerd",
                    "RuntimeVersion": "1.6.x"
                },
                "Tags": null,
                "Taints": [],
                "Unschedulable": 0,
                "UserScript": "#!/bin/sh\ntouch /tmp/after"
            }
        ],
        "RequestId": "efb810cb-d5a2-4147-88ec-cd1e28c5202e",
        "TotalCount": 1
    }
}
```

