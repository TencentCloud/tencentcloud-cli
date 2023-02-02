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
            "NodePoolId": "xx",
            "Name": "xx",
            "ClusterInstanceId": "xx",
            "LifeState": "xx",
            "LaunchConfigurationId": "xx",
            "AutoscalingGroupId": "xx",
            "Labels": [
                {
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "Taints": [
                {
                    "Key": "xx",
                    "Value": "xx",
                    "Effect": "xx"
                }
            ],
            "NodeCountSummary": {
                "ManuallyAdded": {
                    "Joining": 0,
                    "Initializing": 0,
                    "Normal": 0,
                    "Total": 0
                },
                "AutoscalingAdded": {
                    "Joining": 0,
                    "Initializing": 0,
                    "Normal": 0,
                    "Total": 0
                }
            },
            "AutoscalingGroupStatus": "xx",
            "MaxNodesNum": 0,
            "MinNodesNum": 0,
            "DesiredNodesNum": 0,
            "NodePoolOs": "xx",
            "OsCustomizeType": "xx",
            "ImageId": "xx",
            "DesiredPodNum": 0,
            "UserScript": "xx",
            "Tags": [
                {
                    "Key": "xx",
                    "Value": "xx"
                }
            ],
            "DeletionProtection": true,
            "ExtraArgs": {
                "Kubelet": [
                    "xx"
                ]
            },
            "GPUArgs": {
                "MIGEnable": true,
                "Driver": {
                    "Version": "xx",
                    "Name": "xx"
                },
                "CUDA": {
                    "Version": "xx",
                    "Name": "xx"
                },
                "CUDNN": {
                    "Version": "xx",
                    "Name": "xx",
                    "DocName": "xx",
                    "DevName": "xx"
                },
                "CustomDriver": {
                    "Address": "xx"
                }
            },
            "DockerGraphPath": "xx",
            "DataDisks": [
                {
                    "DiskType": "xx",
                    "FileSystem": "xx",
                    "DiskSize": 0,
                    "AutoFormatAndMount": true,
                    "MountTarget": "xx",
                    "DiskPartition": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

