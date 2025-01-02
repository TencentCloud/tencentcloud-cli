**Example 1: 查询集群实例信息**

查询集群实例信息

Input: 

```
tccli tke DescribeClusterInstances --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceSet": [
            {
                "InstanceId": "ins-ocd7e1lx",
                "LanIP": "9.165.0.2",
                "InstanceRole": "WORKER",
                "InstanceState": "running",
                "NodePoolId": "",
                "AutoscalingGroupId": "",
                "FailedReason": "=Ready:True",
                "DrainStatus": "",
                "InstanceAdvancedSettings": {
                    "MountTarget": "",
                    "DockerGraphPath": "",
                    "UserScript": "",
                    "Unschedulable": 0,
                    "Labels": [
                        {
                            "Name": "node-type",
                            "Value": "controller"
                        }
                    ],
                    "Taints": null,
                    "DataDisks": [
                        {
                            "DiskType": "CLOUD_PREMIUM",
                            "FileSystem": "ext4",
                            "DiskSize": 200,
                            "AutoFormatAndMount": true,
                            "MountTarget": "/var/lib/docker",
                            "DiskPartition": ""
                        }
                    ],
                    "ExtraArgs": {
                        "Kubelet": []
                    },
                    "DesiredPodNumber": 32,
                    "GPUArgs": null,
                    "PreStartUserScript": null
                },
                "CreatedTime": "2021-03-09T08:26:51Z"
            }
        ],
        "RequestId": "342ea0aa-e45a-41dd-84f5-f7a2929d3fac"
    }
}
```

