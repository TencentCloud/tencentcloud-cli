**Example 1: 查询节点池详情**

查询节点池详情

Input: 

```
tccli tke DescribeClusterNodePoolDetail --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --NodePoolId np-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "NodePool": {
            "AutoscalingGroupId": "asg-xxx",
            "AutoscalingGroupStatus": "disabled",
            "ClusterInstanceId": "cls-xxx",
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
            "LaunchConfigurationId": "asc-xxx",
            "LifeState": "normal",
            "MaxNodesNum": 3,
            "MinNodesNum": 0,
            "Name": "xxx",
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
            "NodePoolId": "np-xxx",
            "NodePoolOs": "tlinux_xxx",
            "OsCustomizeType": "GENERAL",
            "PreStartUserScript": "#!/bin/sh\ntouch /tmp/before",
            "Tags": null,
            "Taints": [],
            "Unschedulable": 0,
            "UserScript": "#!/bin/sh\ntouch /tmp/after"
        },
        "RequestId": "68b7b080-7c57-4869-bc54-a518b4902b2d"
    }
}
```

